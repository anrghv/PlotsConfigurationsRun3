#!usr/bin/env python
import ROOT
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_auc_score, roc_curve
from xgboost import XGBClassifier
import pickle
import os
import mkShapesRDF

import configHgg_cfg as config

ROOT.gInterpreter.Declare("using namespace ROOT::VecOps;")
ROOT.gErrorIgnoreLevel = ROOT.kError
# /afs/cern.ch/user/a/araghav/Analyses/Run3/mkShapesRDF/mkShapesRDF

headers_path = os.path.join(os.path.dirname(mkShapesRDF.__file__), "include", "headers.hh")

with open(headers_path) as f:
    ROOT.gInterpreter.Declare(f.read())
# ROOT.gInterpreter.Declare('#include "<path>/headers.hh"')

def aliases_applies(sampleName, aliases):
    if 'samples' not in aliases:
        return True
    scope = aliases['samples']
    if isinstance(scope, str):
        return sampleName == scope
    return sampleName in scope

def build_dataframe(sampleName, sample):
    chain = ROOT.TChain("Events")
    for tag, filelist, *rest in sample['name']:
        for f in filelist:
            chain.Add(f)

    df = ROOT.RDataFrame(chain)
    for aliasName, alias in config.aliases.items():
        if aliases_applies(sampleName, alias):
            df = df.Define(aliasName, alias['expr'])
    
    df = df.Filter(config.cut)
    df = df.Define("eventWeight", sample['weight'])
    return df

def runJob():
    isSignalMap = {name: (1 if name in config.signals else 0) for name in config.samples}

    all_X, all_y, all_w = [], [], []

    for sampleName, sample in config.samples.items():
        print("Processing sample:", sampleName)
        df = build_dataframe(sampleName, sample)

        cols = config.mvaVariables + ["eventWeight"]
        data = df.AsNumpy(columns=cols)

        n = len(data["eventWeight"])
        if n == 0:
            print(f"No events found for sample {sampleName}. Skipping.")
            continue
        
        X = np.column_stack([data[v] for v in config.mvaVariables])
        w = data["eventWeight"]
        w = np.abs(w)  # Ensure weights are positive
        y = np.full(n,isSignalMap[sampleName])

        print (f"Sample {sampleName}: {n} events, {np.sum(y)} signal events.")
        all_X.append(X)
        all_y.append(y)
        all_w.append(w)

    X = np.concatenate(all_X)
    y = np.concatenate(all_y)
    w = np.concatenate(all_w)

    X_train, X_test, y_train, y_test, w_train, w_test = train_test_split(X, y, w, test_size=0.2, random_state=42, stratify=y)

    clf = XGBClassifier(
        n_estimators=500,
        max_depth=2,
        learning_rate=0.05,
        subsample=0.5,
        eval_metric = "logloss",
    )

    clf.fit(X_train, y_train, sample_weight=w_train)

    train_scores = clf.predict_proba(X_train)[:, 1]
    test_scores = clf.predict_proba(X_test)[:, 1]

    print("Train AUC:", roc_auc_score(y_train, train_scores, sample_weight=w_train))
    print("Test AUC:", roc_auc_score(y_test, test_scores, sample_weight=w_test))

    with open("xgb_Hgg.pkl", "wb") as f:
        pickle.dump(clf, f)

    np.savez("bdt_Hgg_scores_train.npz", 
              y_train=y_train,train_scores=train_scores, w_train=w_train,
              y_test=y_test, test_scores=test_scores, w_test=w_test)

    for var, imp in zip(config.mvaVariables, clf.feature_importances_):
        print(f"Feature: {var}, Importance: {imp}")

if __name__ == "__main__":
    runJob()
