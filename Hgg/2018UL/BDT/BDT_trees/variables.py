import ROOT
import math


# ==========================================================
# Basic variables
# ==========================================================

def mll(tree):
    return tree.mll


def lep_pt1(tree):
    return tree.Lepton_pt[0]


def lep_pt2(tree):
    return tree.Lepton_pt[1]


# ==========================================================
# QGL helper functions
# ==========================================================

def cleanJet_qgl(tree):
    """
    Equivalent of:
    Take(Jet_qgl, CleanJet_jetIdx)
    """

    qgl = []

    for idx in tree.CleanJet_jetIdx:
        if idx >= 0:
            qgl.append(tree.Jet_qgl[idx])
        else:
            qgl.append(-1.)

    return qgl


def lowestQGLIdx(tree):
    """
    Equivalent of:
    Take(Nonzero(CleanJet_qgl >= 0),
         Argsort(CleanJet_qgl[CleanJet_qgl >= 0]))
    """

    qgl = cleanJet_qgl(tree)

    valid = []

    for i, value in enumerate(qgl):
        if value >= 0:
            valid.append((value, i))

    valid.sort(key=lambda x: x[0])

    return [i for _, i in valid]


def getJet(tree, collection, idx, default):

    indices = lowestQGLIdx(tree)

    if idx >= len(indices):
        return default

    return collection[indices[idx]]


# ==========================================================
# Lowest-QGL jet variables
# ==========================================================

def LowestQGLJet_pt1(tree):
    return getJet(tree, tree.CleanJet_pt, 0, 0.)


def LowestQGLJet_pt2(tree):
    return getJet(tree, tree.CleanJet_pt, 1, 0.)


def LowestQGLJet_pt3(tree):
    return getJet(tree, tree.CleanJet_pt, 2, 0.)


def LowestQGLJet_eta1(tree):
    return getJet(tree, tree.CleanJet_eta, 0, 99.)


def LowestQGLJet_eta2(tree):
    return getJet(tree, tree.CleanJet_eta, 1, 99.)


def LowestQGLJet_phi1(tree):
    return getJet(tree, tree.CleanJet_phi, 0, 99.)


def LowestQGLJet_phi2(tree):
    return getJet(tree, tree.CleanJet_phi, 1, 99.)


def LowestQGLJet_mass1(tree):
    return getJet(tree, tree.CleanJet_mass, 0, 0.)


def LowestQGLJet_mass2(tree):
    return getJet(tree, tree.CleanJet_mass, 1, 0.)


# ==========================================================
# Four-vector helper
# ==========================================================

def jetVector(pt, eta, phi, mass):

    v = ROOT.Math.PtEtaPhiMVector()

    v.SetPt(pt)
    v.SetEta(eta)
    v.SetPhi(phi)
    v.SetM(mass)

    return v


# ==========================================================
# Dijet variables
# ==========================================================

def mjj_qgl(tree):

    idx = lowestQGLIdx(tree)

    if len(idx) < 2:
        return -9999.

    j1 = jetVector(
        tree.CleanJet_pt[idx[0]],
        tree.CleanJet_eta[idx[0]],
        tree.CleanJet_phi[idx[0]],
        tree.CleanJet_mass[idx[0]]
    )

    j2 = jetVector(
        tree.CleanJet_pt[idx[1]],
        tree.CleanJet_eta[idx[1]],
        tree.CleanJet_phi[idx[1]],
        tree.CleanJet_mass[idx[1]]
    )

    return (j1 + j2).M()


def ptjj_qgl(tree):

    idx = lowestQGLIdx(tree)

    if len(idx) < 2:
        return -9999.

    j1 = jetVector(
        tree.CleanJet_pt[idx[0]],
        tree.CleanJet_eta[idx[0]],
        tree.CleanJet_phi[idx[0]],
        tree.CleanJet_mass[idx[0]]
    )

    j2 = jetVector(
        tree.CleanJet_pt[idx[1]],
        tree.CleanJet_eta[idx[1]],
        tree.CleanJet_phi[idx[1]],
        tree.CleanJet_mass[idx[1]]
    )

    return (j1 + j2).Pt()


def detajj_qgl(tree):

    idx = lowestQGLIdx(tree)

    if len(idx) < 2:
        return -9999.

    return abs(
        tree.CleanJet_eta[idx[0]]
        -
        tree.CleanJet_eta[idx[1]]
    )

def drjj_qgl(tree):

    idx = lowestQGLIdx(tree)

    if len(idx) < 2:
        return -9999.

    eta1 = tree.CleanJet_eta[idx[0]]
    eta2 = tree.CleanJet_eta[idx[1]]

    phi1 = tree.CleanJet_phi[idx[0]]
    phi2 = tree.CleanJet_phi[idx[1]]

    dphi = ROOT.TVector2.Phi_mpi_pi(phi1 - phi2)

    return math.sqrt((eta1 - eta2)**2 + dphi**2)