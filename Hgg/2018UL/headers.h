#ifndef HGG_BDT_HEADERS_H
#define HGG_BDT_HEADERS_H

#include <TMVA/RBDT.hxx>
#include <vector>

// 1-Fold evaluation (Single model)
inline float eval_xgboost(
    float mjj_qgl, float dphijj_qgl,
    float LowestQGLJet_eta1, float LowestQGLJet_eta2, float LowestQGLJet_pt1,
    float LowestQGLJet_pt2, float ptjj_qgl, float dphilljetjet_qgl,
    float detajj,  float lep_pt0, float lep_pt1, float ptll

    // float detajj_qgl, float drjj_qgl  ,
    // ,  float drjj, ,
    // float PuppiMET_pt,
) {
    // static ensures the ROOT model file is read from EOS/AFS only ONCE
    static TMVA::Experimental::RBDT bdt(
        "bdt_model", 
        "/eos/user/a/araghav/XGBoost/xgb_model.root"
    );

    // Feature ordering MUST match mvaVariables from training exactly
    std::vector<float> inputs = {
        mjj_qgl, dphijj_qgl, 
        LowestQGLJet_eta1, LowestQGLJet_eta2, LowestQGLJet_pt1, LowestQGLJet_pt2,
        ptjj_qgl, dphilljetjet_qgl,
        detajj,
        lep_pt0, lep_pt1, ptll
        // drjj_qgl , dphijj_qgl,
        // drjj, 
        // PuppiMET_pt,
    };

    return bdt.Compute(inputs)[0];
}

#endif