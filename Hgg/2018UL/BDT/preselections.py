# # preselections

# preselections = (
#     'mll>12'
#     ' && Lepton_pt[0]>25'
#     ' && Lepton_pt[1]>10'
#     ' && Alt$(Lepton_pt,2,0) < 15'
#     ' && (abs(Lepton_pdgId[1])==13 || Lepton_pt[1]>13)'
#     ' && abs(Lepton_eta[0])<2.5 && abs(Lepton_eta[1])<2.5'
#     ' && (abs(Lepton_pdgId[0])==abs(Lepton_pdgId[1]))'
#     # ' && bVeto'
# )

preselections = (
    "mll > 12"
    " && Lepton_pt[0] > 25"
    " && Lepton_pt[1] > 10"
    " && Alt$(Lepton_pt[2],0) < 15"
    " && (abs(Lepton_pdgId[1]) == 13 || Lepton_pt[1] > 13)"
    " && abs(Lepton_eta[0]) < 2.5"
    " && abs(Lepton_eta[1]) < 2.5"
    " && (abs(Lepton_pdgId[0]) == abs(Lepton_pdgId[1]))"
)
# ======================================================================================================================================
# preselections = {}

# preselections['ALL']  = "WH3l_flagOSSF == 0 || WH3l_flagOSSF == 1"

# preselections['SSSF'] = 'WH3l_flagOSSF == 0 \
#                       && Alt$( CleanJet_pt[0], 0) < 30 \
#                       && MinIf$( WH3l_mOSll[], WH3l_mOSll[Iteration$] > 0) > 12 \
#                       && Alt$(Lepton_pt[0],0)>10 \
#                       && Alt$(Lepton_pt[1],0)>10 \
#                       && Alt$(Lepton_pt[2],0)>10 \
#                       && (nLepton>=3 && Alt$(Lepton_pt[3],0)<10) \
#                       && abs(WH3l_chlll) == 1 \
# '

# preselections['OSSF']  = 'WH3l_flagOSSF == 1 \
#                        && WH3l_ZVeto > 20 \
#                        && Alt$( CleanJet_pt[0], 0) < 30 \
#                        && PuppiMET_pt > 50 \
#                        && MinIf$( WH3l_mOSll[], WH3l_mOSll[Iteration$] > 0) > 12 \
#                        && Alt$(Lepton_pt[0],0)>10 \
#                        && Alt$(Lepton_pt[1],0)>10 \
#                        && Alt$(Lepton_pt[2],0)>10 \
#                        && (nLepton>=3 && Alt$(Lepton_pt[3],0)<10) \
#                        && abs(WH3l_chlll) == 1 \
# '