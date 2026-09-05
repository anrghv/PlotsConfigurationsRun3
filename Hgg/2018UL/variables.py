# variables

# 0 = not fold (default), 1 = fold underflowbin, 2 = fold overflow bin, 3 = fold underflow and overflow
    
variables = {}

# variables['ttree_variable'] = {
#         'tree': {'LeptonPt1': 'Lepton_pt[0]'},
#         'cuts': ['sr']
#         }

variables['ptj1'] = {
        'name': 'Alt(CleanJet_pt,0,0)',
        'range': (100, 10, 100),
        'xaxis': 'p_{T} 1st jet',
        'fold' :0
}

variables['ptj2'] = {
        'name': 'Alt(CleanJet_pt,1,0)',
        'range': (100, 10, 100),
        'xaxis': 'p_{T} 2nd jet',
        'fold' :0
}

variables['lowestqgl_ptj1'] = {
        'name': 'LowestQGLJet_pt1',
        'range': (100,10,100),
        'xaxis': 'p_{T} 1st jet(lowestQGL)',
        'fold': 0
}

variables['lowestqgl_ptj2'] = {
        'name': 'LowestQGLJet_pt2',
        'range': (100,10,100),
        'xaxis': 'p_{T} 2nd jet(lowestQGL)',
        'fold': 0
}


variables['qglj1'] = {
        'name': 'Alt(Jet_qgl,CleanJet_jetIdx[0],2)',
        'range': (100, 0, 1),
        'xaxis': 'QGL 1st jet',
        'fold' :2
}

variables['qgl_j1_lowestqgl'] = {
    'name': 'Alt(Take(CleanJet_qgl, LowestQGLIdx), 0, -9999)',
    'range': (100, 0, 0.5),
    'xaxis': 'QGL value 1st jet (lowest QGL)',
    'fold': 2
}


# variables['qglj1morebins'] = {
#         'name': 'Alt(Jet_qgl,CleanJet_jetIdx[0],2)',
#         'range': (20, -0.01, 0.3),
#         'xaxis': 'QGL 1st jet',
#         'fold' :3
# }

variables['qglj2'] = {
        'name': 'Alt(Jet_qgl,CleanJet_jetIdx[1],2)',
        'range': (100, 0, 1),
        'xaxis': 'QGL 2nd jet',
        'fold' :2
}

variables['qgl_j2_lowestqgl'] = {
    'name': 'Alt(Take(CleanJet_qgl, LowestQGLIdx), 1, -9999)',
    'range': (100, 0, 0.5),
    'xaxis': 'QGL value 2nd jet (lowest QGL)',
    'fold': 2
}


variables['etaj1'] = {
        'name': 'Alt(CleanJet_eta,0,0)',
        'range': (100, -5, 5),
        'xaxis': '#eta 1st jet',
        'fold' :3
}

variables['etaj1_lowestqgl'] = {
        'name': 'LowestQGLJet_eta1',
        'range': (100, -5, 5),
        'xaxis': '#eta 1st jet (lowest QGL)',
        'fold' :2
}


variables['etaj2'] = {
        'name': 'Alt(CleanJet_eta,1,0)',
        'range': (100, -5, 5),
        'xaxis': '#eta 2nd jet',
        'fold' :3
}

variables['etaj2_lowestqgl'] = {
        'name': 'LowestQGLJet_eta2',
        'range': (100, -5, 5),
        'xaxis': '#eta 2nd jet (lowest QGL)',
        'fold' :2
}



variables['btagDeepBj1'] = {
        'name': 'Alt(Jet_btagDeepB,CleanJet_jetIdx[0],2)',
        'range': (100, 0, 1),
        'xaxis': 'btagDeepB 1st jet',
        'fold' :0
}

variables['btagDeepBj1_lowestqgl'] = {
    'name': 'btagDeepBj1_lowestqgl',
    'range': (100, 0, 1),
    'xaxis': 'btagDeepB 1st jet (lowest QGL)',
    'fold': 0
}

variables['btagDeepBj2'] = {
        'name': 'Alt(Jet_btagDeepB,CleanJet_jetIdx[1],2)',
        'range': (100, 0, 1),
        'xaxis': 'btagDeepB 2nd jet',
        'fold' :3
}

variables['btagDeepBj2_lowestqgl'] = {
    'name': 'btagDeepBj2_lowestqgl',
    'range': (100, 0, 1),
    'xaxis': 'btagDeepB 2nd jet (lowest QGL)',
    'fold': 0
}


variables['btagCSVV2j1'] = {
        'name': 'Alt(Jet_btagCSVV2,CleanJet_jetIdx[0],2)',
        'range': (100, 0, 1),
        'xaxis': 'btagCSVV2 1st jet',
        'fold' :0
}

variables['btagCSVV2j1_lowestqgl'] = {
    'name': 'btagCSVV2j1_lowestqgl',
    'range': (100, 0, 1),
    'xaxis': 'btagCSVV2 1st jet (lowest QGL)',
    'fold': 0
}

variables['btagCSVV2j2'] = {
        'name': 'Alt(Jet_btagCSVV2,CleanJet_jetIdx[1],2)',
        'range': (100, 0, 1),
        'xaxis': 'btagCSVV2 2nd jet',
        'fold' :0
}

variables['btagCSVV2j2_lowestqgl'] = {
    'name': 'btagCSVV2j2_lowestqgl',
    'range': (100, 0, 1),
    'xaxis': 'btagCSVV2 2nd jet (lowest QGL)',
    'fold': 0
}



#Take(Jet_btagDeepFlavB, CleanJet_jetIdx), 0)
#Jet_btagDeepFlavB[CleanJet_jetIdx[0]]
#Alt(Take(Jet_btagDeepFlavB, CleanJet_jetIdx), 1, -99) -999.99*(CleanJet_pt[1]<20)
#
#Take(Jet_btagDeepFlavB, CleanJet_jetIdx)[0]
#Jet_btagDeepFlavB[CleanJet_jetIdx[0]]
#

variables['mjj']      = {   'name': 'mjj',            #   variable name    
                            'range' : (100, 0, 200),    #   variable range
                            'xaxis' : 'm_{jj} [GeV]',  #   x axis name
                            'fold' :0
                        }

variables['nValidQGL'] = {
    'name': 'CleanJet_qgl_valid.size()',
    'range': (10,0,10),
    'xaxis': 'N valid QGL jets',
    'fold': 3
}


# variables['mjjbins']      = {   'name': 'mjj',            #   variable name    
#                             'range' : (100, 0, 200),    #   variable range
#                             'xaxis' : 'm_{jj} [GeV]',  #   x axis name
#                             'fold' :3
#                         }

variables['ptll']  = {   'name': 'ptll',
                        'range' : (100, 0, 200),
                        'xaxis' : 'p_{T}^{ll} [GeV]',
                        'fold' : 0
                        }

variables['mll']  = {   'name': 'mll',
                        'range' : (100, 0,200),
                        'xaxis' : 'm_{ll} [GeV]',
                        'fold' : 0
                        }


variables['ptl1']  = {   'name': 'Lepton_pt[0]',
                        'range' : (60,0,200),
                        'xaxis' : 'p_{T} 1st lep',
                        'fold'  : 0
                        }


# variables['ptl1lessbins']  = {   'name': 'Lepton_pt[0]',
#                         'range' : (20,0,300),
#                         'xaxis' : 'p_{T} 1st lep',
#                         'fold'  : 3
#                         }

variables['ptl2']  = {   'name': 'Lepton_pt[1]',
                        'range' : (60,0,200),
                        'xaxis' : 'p_{T} 2nd lep',
                        'fold'  : 0
                        }


variables['puppimet']  = {
                        'name': 'PuppiMET_pt',
                        'range' : (100,0,200),
                        'xaxis' : 'puppimet [GeV]',
                        'fold'  : 3
                        }

variables['detajj']  = {  'name': 'detajj',
                        'range' : (100, 0.0, 9.0),
                        'xaxis' : '#Delta#eta_{jj}',
                        'fold'  : 2
                        }

variables['dphijj']  = {  'name': 'dphijj',
                        'range' : (100, -3.5, 3.5),
                        'xaxis' : '#Delta#phi_{jj}',
                        'fold'  : 2
                        }


variables['drjj']  = {  'name': 'drjj',
                        'range' : (100, 0.0, 9.0),
                        'xaxis' : '#DeltaR_{jj}',
                        'fold'  : 2
                        }


#ll jetjet


variables['dphilljet']  = {  'name': 'dphilljet',
                        'range' : (100, 0, 3.5),
                        'xaxis' : '#Delta#phi_{ll,j}',
                        'fold'  : 2
                        }

variables['dphilljet_qgl']  = {  'name': 'dphilljet_qgl',
                        'range' : (100, 0, 3.5),
                        'xaxis' : '#Delta#phi_{ll,j} (lowest QGL)',
                        'fold'  : 2
                        }

variables['dphilljetjet']  = {  'name': 'dphilljetjet',
                        'range' : (100, 0, 3.5),
                        'xaxis' : '#Delta#phi_{ll,jj}',
                        'fold'  : 2
                        }

variables['dphilljetjet_qgl']  = {  'name': 'dphilljetjet_qgl',
                        'range' : (100, 0, 3.5),
                        'xaxis' : '#Delta#phi_{ll,jj} (lowest QGL)',
                        'fold'  : 2
                        }

variables['mjj_qgl']      = {   'name': 'mjj_qgl',            #   variable name    
                            'range' : (100, 0, 200),    #   variable range
                            'xaxis' : 'm_{jj} [GeV]',  #   x axis name
                            'fold' :0
                        }


# variables['mjj_qgl_cc']      = {   'name': 'mjj_qgl_cc',            #   variable name    
#                             'range' : (100, 0, 200),    #   variable range
#                             'xaxis' : 'm_{jj} cc [GeV]',  #   x axis name
#                             'fold' :3
#                         }

variables['detajj_qgl']      = {   'name': 'detajj_qgl',            #   variable name    
                            'range' : (100, 0.0, 9.0),    #   variable range
                            'xaxis' : '#Delta#eta_{jj}',  #   x axis name
                            'fold' :2
                        }

variables['dphijj_qgl']      = {   'name': 'dphijj_qgl',            #   variable name    
                            'range' : (100, -3.5, 3.5),    #   variable range
                            'xaxis' : '#Delta#phi_{jj}',  #   x axis name
                            'fold' :2
                        }

variables['drjj_qgl']      = {   'name': 'drjj_qgl',            #   variable name    
                            'range' : (100, 0.0, 9.0),    #   variable range
                            'xaxis' : '#DeltaR_{jj}',  #   x axis name
                            'fold' :2
                        }

variables['ptjj_qgl']      = {   'name': 'ptjj_qgl',            #   variable name    
                            'range' : (100, 0, 200),    #   variable range
                            'xaxis' : 'pt_{jj} [GeV]',  #   x axis name
                            'fold' :0
                        }

# variables['ptjj']      = {   'name': 'ptjj',            #   variable name    
#                             'range' : (100, 0, 200),    #   variable range
#                             'xaxis' : 'pt_{jj} [GeV]',  #   x axis name
#                             'fold' :0
#                         }