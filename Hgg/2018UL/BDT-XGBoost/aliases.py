import os
import copy
import inspect
# import configuration

# configurations = os.path.realpath(inspect.getfile(inspect.currentframe())) # this file
# configurations = os.path.dirname(configurations) # Full2018_v7
# configurations = os.path.dirname(configurations) # BDTconfig
# configurations = os.path.dirname(configurations) # WH3l
# configurations = os.path.dirname(configurations) # WH_chargeAsymmetry
# configurations = os.path.dirname(configurations) # Configurations

aliases = {}
# aliases = OrderedDict()

with open("configuration.py") as handle:
    exec(handle.read())

samples={}
structure={}
cuts={}
for f in [samplesFile, structureFile, cutsFile]:
    with open(f) as handle:
        exec(handle.read())

# imported from samples.py:
# samples, signals

mc = [skey for skey in samples if skey not in ('Fake', 'DATA')]
mc_special = [skey for skey in samples if skey not in ('Fake', 'DATA', 'Hgluglu', 'qqZHgluglu', 'ggZHgluglu')]

eleWP = 'mvaFall17V2Iso_WP90'
muWP = 'cut_Tight_HWWW'

aliases['LepWPCut'] = {
    'expr' : 'LepCut2l__ele_mvaFall17V2Iso_WP90__mu_cut_Tight_HWWW*\
     ( ((abs(Lepton_pdgId[0])==13 && Muon_mvaTTH[Lepton_muonIdx[0]]>0.82) || (abs(Lepton_pdgId[0])==11 && Lepton_mvaTTH_UL[0]>0.90)) \
    && ((abs(Lepton_pdgId[1])==13 && Muon_mvaTTH[Lepton_muonIdx[1]]>0.82) || (abs(Lepton_pdgId[1])==11 && Lepton_mvaTTH_UL[1]>0.90)) )',
    #'samples': mc + ['DATA']
    'samples': mc_special + ['DATA']
}
aliases['CleanJet_qgl'] = {
    'expr': 'Take(Jet_qgl, CleanJet_jetIdx)'
}

aliases['CleanJet_qgl_valid'] = {
    'expr': 'CleanJet_qgl[CleanJet_qgl >= 0]'
}

aliases['LowestQGLIdx'] = {
    'expr': 'Take(Nonzero(CleanJet_qgl >= 0), Argsort(CleanJet_qgl[CleanJet_qgl >= 0]))'
}

aliases['LowestQGLJet_pt1'] = {
    'expr': 'Alt(CleanJet_pt, LowestQGLIdx[0], 0)'
}

aliases['LowestQGLJet_pt2'] = {
    'expr': 'Alt(CleanJet_pt, LowestQGLIdx[1], 0)'
}

aliases['LowestQGLJet_pt3'] = {
    'expr': 'Alt(CleanJet_pt, LowestQGLIdx[2], 0)'
}

aliases['LowestQGLJet_eta1'] = {
    'expr': 'Alt(CleanJet_eta, LowestQGLIdx[0], 99)'
}

aliases['LowestQGLJet_eta2'] = {
    'expr': 'Alt(CleanJet_eta, LowestQGLIdx[1], 99)'
}

aliases['LowestQGLJet_phi1'] = {
    'expr': 'Alt(CleanJet_phi, LowestQGLIdx[0], 99)'
}

aliases['LowestQGLJet_phi2'] = {
    'expr': 'Alt(CleanJet_phi, LowestQGLIdx[1], 99)'
}

aliases['LowestQGLJet_mass1'] = {
    'expr': 'Alt(CleanJet_mass, LowestQGLIdx[0], 0)'
}

aliases['LowestQGLJet_mass2'] = {
    'expr': 'Alt(CleanJet_mass, LowestQGLIdx[1], 0)'
}

aliases['mjj_qgl'] = {
    'expr': 'LowestQGLIdx.size() >= 2 ? (ROOT::Math::PtEtaPhiMVector(CleanJet_pt[LowestQGLIdx[0]],CleanJet_eta[LowestQGLIdx[0]],CleanJet_phi[LowestQGLIdx[0]],CleanJet_mass[LowestQGLIdx[0]])+ROOT::Math::PtEtaPhiMVector(CleanJet_pt[LowestQGLIdx[1]],CleanJet_eta[LowestQGLIdx[1]],CleanJet_phi[LowestQGLIdx[1]],CleanJet_mass[LowestQGLIdx[1]])).M() : -9999.0'
}

aliases['detajj_qgl'] = {
    'expr': 'LowestQGLIdx.size() >= 2 ? abs(LowestQGLJet_eta1 - LowestQGLJet_eta2) : -9999.0'
}

aliases['ptjj_qgl'] = {
    'expr': 'LowestQGLIdx.size() >= 2 ? (ROOT::Math::PtEtaPhiMVector(CleanJet_pt[LowestQGLIdx[0]], CleanJet_eta[LowestQGLIdx[0]], CleanJet_phi[LowestQGLIdx[0]], CleanJet_mass[LowestQGLIdx[0]]) + ROOT::Math::PtEtaPhiMVector(CleanJet_pt[LowestQGLIdx[1]], CleanJet_eta[LowestQGLIdx[1]], CleanJet_phi[LowestQGLIdx[1]], CleanJet_mass[LowestQGLIdx[1]])).Pt() : -9999.0'
}

aliases['drjj_qgl'] = {
    'expr': 'LowestQGLIdx.size() >= 2 ? DeltaR(LowestQGLJet_eta1, LowestQGLJet_eta2, LowestQGLJet_phi1, LowestQGLJet_phi2) : -9999.0'
}

aliases['LepWPSF'] = {
    'expr' : 'LepSF2l__ele_'+eleWP+'__mu_'+muWP,
    #'samples' : mc
    'samples' : mc_special
}

aliases['gstarLow'] = {
    'expr': 'Gen_ZGstar_mass > 0 && Gen_ZGstar_mass < 4',
    'samples': 'VgS'
}

aliases['gstarHigh'] = {
    'expr': 'Gen_ZGstar_mass < 0 || Gen_ZGstar_mass > 4',
    'samples': 'WZ'
}

aliases['zeroJet'] = {
    'expr': 'Alt(CleanJet_pt, 0, 0) < 30.'
}

aliases['oneJet'] = {
    'expr': 'Alt(CleanJet_pt, 0, 0) > 30. && Alt(CleanJet_pt, 1, 0) < 30.'
}

aliases['multiJet'] = {
    'expr': 'Alt(CleanJet_pt, 1, 0) > 30.'
}

bWP_loose_deepB  = '0.1208'
bWP_medium_deepB = '0.4168' 
bWP_tight_deepB  = '0.7665'

bAlgo = 'DeepB'          # ['DeepB',        'DeepFlavB'         ]
bWP   = bWP_medium_deepB # [bWP_loose_deepB, bWP_loose_deepFlavB]
bSF   = 'deepcsv'       

# b veto
aliases['bVeto'] = {
    'expr': 'Sum(CleanJet_pt > 20. && abs(CleanJet_eta) < 2.5 && Take(Jet_btag{}, CleanJet_jetIdx) > {}) == 0'.format(bAlgo, bWP)
}

aliases['bVetoSF'] = {
    'expr': 'TMath::Exp(Sum(LogVec((CleanJet_pt>20 && abs(CleanJet_eta)<2.5)*Take(Jet_btagSF_{}_shape, CleanJet_jetIdx)+1*(CleanJet_pt<20 || abs(CleanJet_eta)>2.5))))'.format(bSF),
    #'samples': mc
    'samples' : mc_special
}

# At least one b-tagged jet
aliases['bReq'] = {
    'expr': 'Sum(CleanJet_pt > 30. && abs(CleanJet_eta) < 2.5 && Take(Jet_btag{}, CleanJet_jetIdx) > {}) >= 1'.format(bAlgo, bWP)
}

aliases['bReqSF'] = {
    'expr': 'TMath::Exp(Sum(LogVec((CleanJet_pt>30 && abs(CleanJet_eta)<2.5)*Take(Jet_btagSF_{}_shape, CleanJet_jetIdx)+1*(CleanJet_pt<30 || abs(CleanJet_eta)>2.5))))'.format(bSF),
    #'samples': mc
    'samples' : mc_special
}

# Top control region
aliases['topcr'] = {
    'expr': 'mtw2>30 && mll>50 && ((zeroJet && !bVeto) || bReq)'
}

# WW control region
aliases['wwcr'] = {
    'expr': 'mth>60 && mtw2>30 && mll>100 && bVeto'
}

# Overall b tag SF
aliases['btagSF'] = {
    'expr': '(bVeto || (topcr && zeroJet))*bVetoSF + (topcr && !zeroJet)*bReqSF',
    #'samples': mc
    'samples' : mc_special
}

# Fake leptons transfer factor
eleFWP = 'mvaFall17V1Iso_WP90_tthmva_70'
muFWP = 'cut_Tight_HWWW_tthmva_80'


aliases['Jet_PUIDSF'] = {
  'expr' : 'TMath::Exp(Sum((Jet_jetId>=2)*LogVec(Jet_PUIDSF_loose)))',
  #'samples': mc
  'samples' : mc_special
}

aliases['PromptGenLepMatch2l'] = {
    'expr': 'Alt(Lepton_promptgenmatched, 0, 0) * Alt(Lepton_promptgenmatched, 1, 0)',
    #'samples': mc
    'samples' : mc_special
}
aliases['Top_pTrw'] = {
    'expr': '(topGenPt * antitopGenPt > 0.) * (TMath::Sqrt(TMath::Exp(0.0615 - 0.0005 * topGenPt) * TMath::Exp(0.0615 - 0.0005 * antitopGenPt))) + (topGenPt * antitopGenPt <= 0.)',
    'samples': ['top']
}

aliases['SFweight'] = {
    #'expr': ' * '.join(['SFweight2l', 'LepWPCut', 'LepWPSF','Jet_PUIDSF', 'btagSF', 'LepWPttHMVASF']),
    'expr': ' * '.join(['SFweight2l', 'LepWPCut', 'LepWPSF','Jet_PUIDSF', 'btagSF']),
    #'samples': mc
    'samples' : mc_special
}
