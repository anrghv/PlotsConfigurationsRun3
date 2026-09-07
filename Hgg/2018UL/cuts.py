# cuts

cuts = {}
# cuts['signal_region_bdt'] = 'bdt_score > 0.65'

preselections = 'mll>12  \
              && Lepton_pt[0]>25 \
              && Lepton_pt[1]>10 \
              && Alt(Lepton_pt,2,0) < 15 \
              && (abs(Lepton_pdgId[1])==13 || Lepton_pt[1]>13) \
              && abs(Lepton_eta[0])<2.5 && abs(Lepton_eta[1])<2.5 \
              && (abs(Lepton_pdgId[0])==abs(Lepton_pdgId[1])) \
              && bVeto \
              '

              #&& bVeto \
              #&& PuppiMET_pt > 30 \
              #&& !hole_veto \


## Same-sign control region in the 0 jet bin: used in the WH3l category. Considering different flavor to avoid DY
#cuts['wh3l_13TeV_OS_CR'] = {
    #'expr' : 'Alt(Lepton_pt,2,0) < 15 && abs(Lepton_pdgId[0]*Lepton_pdgId[1]) == 11*13 && Alt(CleanJet_pt,0,0) < 30',
    #'categories' : {
        #'pt2ge20'  : 'Lepton_pdgId[0]*Lepton_pdgId[1]<0',
    #}
#}


'''
cuts['DY'] = {
    'expr' : 'Alt(Lepton_pt,2,0) < 15 && (abs(Lepton_pdgId[0])==abs(Lepton_pdgId[1]))',
    'categories' : {
        '0j'  : 'Alt(CleanJet_pt,0,0) < 30',
        '1j'  : 'Alt(CleanJet_pt,1,0) < 30 && Alt(CleanJet_pt,0,0) > 30',
        '2j'  : 'Alt(CleanJet_pt,2,0) < 30 && Alt(CleanJet_pt,1,0) > 30',
    }
}
    


cuts['Sig'] = {
    'expr' : 'Alt(Lepton_pt,2,0) < 15 && (abs(Lepton_pdgId[0])==abs(Lepton_pdgId[1])) && Alt(CleanJet_pt,2,0) < 30 && Alt(CleanJet_pt,1,0) > 30',
    'categories' : {
        'mllZ'               : 'mll>60 && mll< 120',
        'mllZpt1'            : 'mll>80 && mll< 100 && Lepton_pt[0]>40',
        'mllZpt1qgl'         : 'mll>80 && mll< 100 && Lepton_pt[0]>40 && Sort(CleanJet_qgl_valid)[0]<0.5 && Sort(CleanJet_qgl_valid)[1]<0.5',
        'mllZpt1qglmet'      : 'mll>80 && mll< 100 && Lepton_pt[0]>40 && Sort(CleanJet_qgl_valid)[0]<0.5 && Sort(CleanJet_qgl_valid)[1]<0.5 && PuppiMET_pt<60',
        'mllZpt1qglmetbVeto' : 'mll>80 && mll< 100 && Lepton_pt[0]>40 && Sort(CleanJet_qgl_valid)[0]<0.5 && Sort(CleanJet_qgl_valid)[1]<0.5 && PuppiMET_pt<60 && bVeto',
        'opt1'               : 'mll>80 && mll< 100 && Lepton_pt[0]>40 && Sort(CleanJet_qgl_valid)[0]<0.5 && Sort(CleanJet_qgl_valid)[1]<0.5 && PuppiMET_pt<60 && bVeto && detajj<3',
        'opt2'               : 'mll>80 && mll< 100 && Lepton_pt[0]>40 && Sort(CleanJet_qgl_valid)[0]<0.5 && Sort(CleanJet_qgl_valid)[1]<0.5 && PuppiMET_pt<60 && bVeto && detajj<3 && mjj<160 && mjj>60 && dphilljetjet>1',
        'opt3'               : 'mll>80 && mll< 100 && Lepton_pt[0]>40 && Sort(CleanJet_qgl_valid)[0]<0.5 && Sort(CleanJet_qgl_valid)[1]<0.5 && PuppiMET_pt<60 && bVeto && detajj<3 && mjj<160 && mjj>60 && dphilljetjet>1 && Alt(Jet_btagDeepB,CleanJet_jetIdx[0],2)<0.2 && Alt(Jet_btagDeepB,CleanJet_jetIdx[1],2) < 0.2 && Alt(Jet_btagCSVV2,CleanJet_jetIdx[0],2)<0.7 && Alt(Jet_btagCSVV2,CleanJet_jetIdx[1],2)<0.7',
        'opt4'               : 'mll>80 && mll< 100 && Lepton_pt[0]>40 && Sort(CleanJet_qgl_valid)[0]<0.5 && Sort(CleanJet_qgl_valid)[1]<0.5 && PuppiMET_pt<60 && bVeto && detajj<2 && mjj<150 && mjj>60 && dphilljetjet>1 && Alt(Jet_btagDeepB,CleanJet_jetIdx[0],2)<0.2 && Alt(Jet_btagDeepB,CleanJet_jetIdx[1],2) < 0.2 && Alt(Jet_btagCSVV2,CleanJet_jetIdx[0],2)<0.7 && Alt(Jet_btagCSVV2,CleanJet_jetIdx[1],2)<0.7 && ptll>20 && Alt(CleanJet_pt,0,0) > 50',
        'opt5future'         : 'mll>85 && mll< 95 && Lepton_pt[0]>40 && Sort(CleanJet_qgl_valid)[0]<0.1 && Sort(CleanJet_qgl_valid)[1]<0.1 && PuppiMET_pt<60 && bVeto && detajj<2 && mjj<150 && mjj>60 && dphilljetjet>1 && Alt(Jet_btagDeepB,CleanJet_jetIdx[0],2)<0.2 && Alt(Jet_btagDeepB,CleanJet_jetIdx[1],2) < 0.2 && Alt(Jet_btagCSVV2,CleanJet_jetIdx[0],2)<0.7 && Alt(Jet_btagCSVV2,CleanJet_jetIdx[1],2)<0.7 && ptll>20 && Alt(CleanJet_pt,0,0) > 50 && Alt(CleanJet_eta,1,0) < 2.5 && Alt(CleanJet_eta,1,0) > -2.5 && Alt(CleanJet_eta,0,0) < 2.5 && Alt(CleanJet_eta,0,0) > -2.5 && Alt(Lepton_pt,0,0)>50',
        'opt6future'         : 'mll>85 && mll< 95 && Lepton_pt[0]>40 && Sort(CleanJet_qgl_valid)[0]<0.04 && Sort(CleanJet_qgl_valid)[1]<0.04 && PuppiMET_pt<60 && bVeto && detajj<2 && mjj<150 && mjj>60 && dphilljetjet>1 && Alt(Jet_btagDeepB,CleanJet_jetIdx[0],2)<0.2 && Alt(Jet_btagDeepB,CleanJet_jetIdx[1],2) < 0.2 && Alt(Jet_btagCSVV2,CleanJet_jetIdx[0],2)<0.7 && Alt(Jet_btagCSVV2,CleanJet_jetIdx[1],2)<0.7 && ptll>20 && Alt(CleanJet_pt,0,0) > 75 && Alt(CleanJet_eta,1,0) < 2.0 && Alt(CleanJet_eta,1,0) > -2.0 && Alt(CleanJet_eta,0,0) < 2.0 && Alt(CleanJet_eta,0,0) > -2.0 && Alt(Lepton_pt,0,0)>50 && ptll>100 && Lepton_pt[1]>20',
        
    }
}
'''
'''
cuts['lowest_qgl_jets'] = {
    'expr' : 'Sort(CleanJet_qgl_valid)[0]<0.5 && Sort(CleanJet_qgl_valid)[1]<0.5',
    'categories' : {
        'mllZ'          : 'mll>80 && mll< 100',
        'mllZpt1'       : 'mll>80 && mll< 100 && Lepton_pt[0]>40',
        'mllZpt1jetpt20'  : 'mll>80 && mll< 100 && Lepton_pt[0]>40 && LowestQGLJet_pt1 > 20 && LowestQGLJet_pt2 > 20',
        'mllZpt1jetpt25'  : 'mll>80 && mll< 100 && Lepton_pt[0]>40 && LowestQGLJet_pt1 > 25 && LowestQGLJet_pt2 > 25',
        'mllZpt1jetpt30'  : 'mll>80 && mll< 100 && Lepton_pt[0]>40 && LowestQGLJet_pt1 > 30 && LowestQGLJet_pt2 > 30',
        'central20'       : 'mll>80 && mll< 100 && Lepton_pt[0]>40 && LowestQGLJet_pt1 > 20 && LowestQGLJet_pt2 > 20 && abs(LowestQGLJet_eta1)<2.5 && abs(LowestQGLJet_eta2)<2.5',
        'central25'       : 'mll>80 && mll< 100 && Lepton_pt[0]>40 && LowestQGLJet_pt1 > 25 && LowestQGLJet_pt2 > 25 && abs(LowestQGLJet_eta1)<2.5 && abs(LowestQGLJet_eta2)<2.5',
        'central30'       : 'mll>80 && mll< 100 && Lepton_pt[0]>40 && LowestQGLJet_pt1 > 30 && LowestQGLJet_pt2 > 30 && abs(LowestQGLJet_eta1)<2.5 && abs(LowestQGLJet_eta2)<2.5',
        #'forward'       : 'mll>80 && mll< 100 && Lepton_pt[0]>40 && LowestQGLJet_pt1 > 20 && LowestQGLJet_pt2 > 20 && !(abs(LowestQGLJet_eta1)<2.5 && abs(LowestQGLJet_eta2)<2.5)',

    }
}
'''
'''
cuts['Highest_pt_jets'] = {
    'expr' : 'Alt(Jet_qgl,CleanJet_jetIdx[0],2)<0.5 && Alt(Jet_qgl,CleanJet_jetIdx[1],2)<0.5',
    'categories' : {
        'mllZ'          : 'mll>80 && mll< 100',
        'mllZpt1'       : 'mll>80 && mll< 100 && Lepton_pt[0]>40',
        'mllZpt1jetpt'  : 'mll>80 && mll< 100 && Lepton_pt[0]>40 && Alt(CleanJet_pt,2,0) < 15 && Alt(CleanJet_pt,1,0) > 30 && Alt(CleanJet_pt,0,0) > 30',
        'central'       : 'mll>80 && mll< 100 && Lepton_pt[0]>40 && Alt(CleanJet_pt,2,0) < 15 && Alt(CleanJet_pt,1,0) > 30 && Alt(CleanJet_pt,0,0) > 30 && abs(CleanJet_eta[0])<2.5 && abs(CleanJet_eta[1])<2.5',
        'forward'       : 'mll>80 && mll< 100 && Lepton_pt[0]>40 && Alt(CleanJet_pt,2,0) < 15 && Alt(CleanJet_pt,1,0) > 30 && Alt(CleanJet_pt,0,0) > 30 && !(abs(CleanJet_eta[0])<2.5 && abs(CleanJet_eta[1])<2.5)',

    }
}
'''

cuts['Sig'] = {

    'expr': 'mll > -9999',

    'categories': {

        'nocut':
            'mll > -9999',

        'mllZ':
            'mll>80 && mll<100 && QGLcut',

        'mllZpt1':
            'mll>80 && mll<100 && Lepton_pt[0]>40 && QGLcut',

        'mllZpt1jetpt':
            'mll>80 && mll<100 && Lepton_pt[0]>40 && LowestQGLJet_pt1>18 && LowestQGLJet_pt2>18 && QGLcut',

        'central':
            'mll>80 && mll<100 && Lepton_pt[0]>40 && LowestQGLJet_pt1>18 && LowestQGLJet_pt2>18 && abs(LowestQGLJet_eta1)<2.8 && abs(LowestQGLJet_eta2)<2.8 && QGLcut',

        'centraldeta':
            'mll>80 && mll<100 && Lepton_pt[0]>40 && LowestQGLJet_pt1>20 && LowestQGLJet_pt2>20 && abs(LowestQGLJet_eta1)<2.8 && abs(LowestQGLJet_eta2)<2.8 && detajj_qgl<2.5 && QGLcut',

        'centraldetamjj':
            'mll>80 && mll<100 && Lepton_pt[0]>40 && LowestQGLJet_pt1>20 && LowestQGLJet_pt2>20 && abs(LowestQGLJet_eta1)<2.5 && abs(LowestQGLJet_eta2)<2.5 && detajj_qgl<2.0 && mjj_qgl>75.0 && mjj_qgl<150.0 && QGLcut',

        'centraldetamjjdR':
            'mll>80 && mll<100 && Lepton_pt[0]>40 && LowestQGLJet_pt1>20 && LowestQGLJet_pt2>20 && abs(LowestQGLJet_eta1)<2.5 && abs(LowestQGLJet_eta2)<2.5 && detajj_qgl<2.0 && mjj_qgl>75.0 && mjj_qgl<150.0 && drjj_qgl<3.8 && QGLcut',

        'centraldetamjjdRptjj':
            'mll>80 && mll<100 && Lepton_pt[0]>40 && LowestQGLJet_pt1>20 && LowestQGLJet_pt2>20 && abs(LowestQGLJet_eta1)<2.5 && abs(LowestQGLJet_eta2)<2.5 && detajj_qgl<2.0 && mjj_qgl>75.0 && mjj_qgl<150.0 && drjj_qgl<3.4 && ptjj_qgl>20.0 && QGLcut',

        'centraldetamjjdRptjjdphijj':
            'mll>80 && mll<100 && Lepton_pt[0]>40 && LowestQGLJet_pt1>20 && LowestQGLJet_pt2>20 && abs(LowestQGLJet_eta1)<2.5 && abs(LowestQGLJet_eta2)<2.5 && detajj_qgl<2.0 && mjj_qgl>75.0 && mjj_qgl<150.0 && drjj_qgl<3.4 && ptjj_qgl>20.0 && dphijj_qgl<2.4 && QGLcut',

        'centraldetamjjdRptjjdphijjJetQgl_BDT':
            'mll>80 && mll<100 && Lepton_pt[0]>40 && LowestQGLJet_pt1>20 && LowestQGLJet_pt2>20 && abs(LowestQGLJet_eta1)<2.5 && abs(LowestQGLJet_eta2)<2.5 && detajj_qgl<2.0 && mjj_qgl>75.0 && mjj_qgl<150.0 && drjj_qgl<3.4 && ptjj_qgl>20.0 && dphijj_qgl<2.4 && qgl_j1_lowestqgl<0.4 && QGLcut && bdt_score>0.65',
    }
}