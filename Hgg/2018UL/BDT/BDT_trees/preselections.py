
def pass_preselection(tree):
 # call bVeto function to check for b-jet veto
    # mll  
    if tree.mll <= 12:
        return False

    # Leading lepton pT
    if tree.Lepton_pt[0] <= 25:
        return False

    # Subleading lepton pT
    if tree.Lepton_pt[1] <= 10:
        return False

    # Third lepton veto
    if len(tree.Lepton_pt) > 2 and tree.Lepton_pt[2] >= 15:
        return False

    # Muon trigger requirement
    if abs(tree.Lepton_pdgId[1]) != 13 and tree.Lepton_pt[1] <= 13:
        return False

    # Eta cuts
    if abs(tree.Lepton_eta[0]) >= 2.5:
        return False

    if abs(tree.Lepton_eta[1]) >= 2.5:
        return False

    # Same flavour
    if abs(tree.Lepton_pdgId[0]) != abs(tree.Lepton_pdgId[1]):
        return False

    # b-veto
    if not bVeto(tree):
        return False

    return True


def bVeto(tree):

    for iJet, jet_pt in enumerate(tree.CleanJet_pt):

        if jet_pt <= 20:
            continue

        if abs(tree.CleanJet_eta[iJet]) >= 2.5:
            continue

        jetIdx = tree.CleanJet_jetIdx[iJet]

        if tree.Jet_btagDeepB[jetIdx] > 0.4168:
            return False

    return True

