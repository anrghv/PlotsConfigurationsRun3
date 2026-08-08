#!/usr/bin/env python

from __future__ import print_function
import os
from ROOT import gROOT, TFile, TChain, TCut

isDEV=True

# Load configuration
# why not import it directly?  
with open("configuration.py") as handle:
    exec(handle.read())

samples={}
structure={}
cuts={}
for f in [samplesFile, structureFile, cutsFile]:
    with open(f) as handle:
        exec(handle.read())

aliases = {}
with open("aliases.py") as handle:
    exec(handle.read())


# Reduce sample files for fast dev
if isDEV:
    print("Running in DEV mode, limiting number of files per sample to: ", limitFiles)
    for sampleName, sample in list(samples.items()):
        if sampleName not in ['Hgluglu', 'DY', 'top', 'Vg', 'VgS', 'WZ', 'ZZ']:
        # if sampleName not in ['Hgluglu', 'qqZHgluglu', 'ggZHgluglu', 'DY', 'top', 'Vg', 'VgS', 'WZ', 'ZZ']:
            samples.pop(sampleName)

# Define data to be loaded
# We already imported preselections, why not use it directly?
with open("./preselections.py") as handle:
    exec(handle.read())

cut="(({0}) && ({1}))".format(supercut,preselections)
# cut = (
#     preselections
#     + " && ("
#     + aliases["bVeto"]["expr"]
#     + ")"
# )



mvaVariables = [
    'mll',
    # 'Lepton_pt[0]',
    # 'Lepton_pt[1]',
    # 'PuppiMET_pt',
    #  "LowestQGLIdx"
    'LowestQGLJet_pt1',
    # 'LowestQGLJet_pt2',
    # 'LowestQGLJet_eta1',
    # 'LowestQGLJet_eta2',
    # 'mjj_qgl',
    # 'detajj_qgl',
    # 'ptjj_qgl',
    # 'drjj_qgl',
]