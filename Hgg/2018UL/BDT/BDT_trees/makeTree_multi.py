import ROOT
from array import array
import os, glob
import time
from preselections import pass_preselection
from variables import *
# ROOT.ROOT.EnableImplicitMT()
from concurrent.futures import ProcessPoolExecutor, as_completed
import multiprocessing

ROOT.gErrorIgnoreLevel = ROOT.kFatal

# MC:   /eos/cms/store/group/phys_higgs/cmshww/amassiro/HWWNano/Summer20UL18_106x_nAODv9_Full2018v9/MCl1loose2018v9__MCCorr2018v9NoJERInHorn__l2tightOR2018v9/
# DATA: /eos/cms/store/group/phys_higgs/cmshww/amassiro/HWWNano/Run2018_UL2018_nAODv9_Full2018v9/DATAl1loose2018v9__l2loose__l2tightOR2018v9/
# FAKE: /eos/cms/store/group/phys_higgs/cmshww/amassiro/HWWNano/Run2018_UL2018_nAODv9_Full2018v9/DATAl1loose2018v9__l2loose__fakeW/

mcProduction = 'Summer20UL18_106x_nAODv9_Full2018v9'
dataReco     = 'Run2018_UL2018_nAODv9_Full2018v9'
mcSteps      = 'MCl1loose2018v9__MCCorr2018v9NoJERInHorn__l2tightOR2018v9'
fakeSteps    = 'DATAl1loose2018v9__l2loose__fakeW'
dataSteps    = 'DATAl1loose2018v9__l2loose__l2tightOR2018v9'

treeBaseDir = '/eos/cms/store/group/phys_higgs/cmshww/amassiro/HWWNano'
limitFiles = -1
# limitFiles = 1


if limitFiles != -1:
    print("Limiting the number of files to %d" % limitFiles)

def makeMCDirectory(var=''):
    return os.path.join(treeBaseDir, mcProduction, mcSteps.format(var=''))

mcDirectory   = makeMCDirectory()
# fakeDirectory = os.path.join(treeBaseDir, dataReco, fakeSteps)
# dataDirectory = os.path.join(treeBaseDir, dataReco, dataSteps)

print("Running with the following directories:")
print (" mcDirectory = " , mcDirectory)
# print (" fakeDirectory = " , fakeDirectory)
# print (" dataDirectory = " , dataDirectory)

samples = {}
from mkShapesRDF.lib.search_files import SearchFiles
s = SearchFiles()

useXROOTD = True
redirector = 'root://eoscms.cern.ch/'


def nanoGetSampleFiles(path, name):   # it is doing the same as searchFiles but with a limit on the number of files
    # print ("nanoGetSampleFiles!")
    _files = s.searchFiles(path, name, redirector=redirector)
    if limitFiles != -1 and len(_files) > limitFiles:
        return [(name, _files[:limitFiles])]
    else:
        return [(name, _files)]

def nanoGetLocalSampleFiles(path, name):  # it is doing the same as searchFiles but with a limit on the number of files. the difference with nanoGetSampleFiles is that it does not use the redirector, so it is used for local files
    # print ("nanoGetLocalSampleFiles!")
    _files = s.searchFiles(path, name, redirector='')
    if limitFiles != -1 and len(_files) > limitFiles:
        return [(name, _files[:limitFiles])]
    else:
        return [(name, _files)]


########## Signal Samples #########
print("\n------------------------------------------------------------------------------")
print("Getting the list of files for the signal samples...\n")
files_ZHgg = nanoGetLocalSampleFiles("/eos/user/a/amassiro/HIG/ZHggPostProc/Summer20UL18_106x_nAODv9_Full2018v9/MCFull2018v9/", "ZHgg")
# print (" list of files Hgg = ", files_ZHgg)
# print(" number of files Hgg = ", len(files_ZHgg[0][1]))

files_ZHllHgg = nanoGetLocalSampleFiles("/eos/user/a/amassiro/HIG/ZHggPostProc/Summer20UL18_106x_nAODv9_Full2018v9/MCFull2018v9/", "ZHllHgg")
# print (" list of files ZHllHgg = ", files_ZHllHgg)
# print(" number of files ZHllHgg = ", len(files_ZHllHgg[0][1]))

files_ggZHllHgg = nanoGetLocalSampleFiles("/eos/user/a/amassiro/HIG/ZHggPostProc/Summer20UL18_106x_nAODv9_Full2018v9/MCFull2018v9/", "ggZHllHgg")
# print (" list of files ggZHllHgg = ", files_ggZHllHgg)
# print(" number of files ggZHllHgg = ", len(files_ggZHllHgg[0][1]))
print("------------------------------------------------------------------------------")


###########################################
#############  BACKGROUNDS  ###############
###########################################

########## Signal Samples #########
print("\n------------------------------------------------------------------------------")
print("Getting the list of files for the Background samples...\n")
############ DY ############

files_DY = nanoGetSampleFiles(mcDirectory, 'DYJetsToLL_M-10to50_NLO') + \
        nanoGetSampleFiles(mcDirectory, 'DYJetsToLL_M-50')
# print("DY files = ", len(files_DY[0][1]))
# print("DY files = ", len(files_DY[0][1])+ len(files_DY[1][1]))

##### Top #######

files_top = nanoGetSampleFiles(mcDirectory, 'TTTo2L2Nu') + \
        nanoGetSampleFiles(mcDirectory, 'ST_s-channel') + \
        nanoGetSampleFiles(mcDirectory, 'ST_t-channel_top') + \
        nanoGetSampleFiles(mcDirectory, 'ST_t-channel_antitop') + \
        nanoGetSampleFiles(mcDirectory, 'ST_tW_antitop') + \
        nanoGetSampleFiles(mcDirectory, 'ST_tW_top')
# print("Top files = ", len(files_top[0][1])+
#       len(files_top[1][1]) + \
#       len(files_top[2][1]) + \
#       len(files_top[3][1]) + \
#       len(files_top[4][1]) + \
#       len(files_top[5][1])  )

######## Vg ########
files_Vg = nanoGetSampleFiles(mcDirectory, 'Wg_AMCNLOFXFX_01J') + \
        nanoGetSampleFiles(mcDirectory, 'ZGToLLG')
# print("Vg files = ", len(files_Vg[0][1])+len(files_Vg[1][1]))

######## VgS ######## 
files_VgS = nanoGetSampleFiles(mcDirectory, 'Wg_AMCNLOFXFX_01J') + \
        nanoGetSampleFiles(mcDirectory, 'WZTo3LNu_mllmin0p1') + \
        nanoGetSampleFiles(mcDirectory, 'ZGToLLG')
# print("VgS files = ", len(files_VgS[0][1])+len(files_VgS[1][1])+len(files_VgS[2][1]))

############ WZ ############
files_WZ = nanoGetSampleFiles(mcDirectory, 'WZTo3LNu_mllmin0p1') + \
        nanoGetSampleFiles(mcDirectory, 'WZTo2Q2L_mllmin4p0')
# print("WZ files = ", len(files_WZ[0][1]) + len(files_WZ[1][1]))

files_ZZ = nanoGetSampleFiles(mcDirectory, 'ZZTo2L2Nu') + \
        nanoGetSampleFiles(mcDirectory, 'ZZTo2Q2L_mllmin4p0') + \
        nanoGetSampleFiles(mcDirectory, 'ZZTo4L')
# print("ZZ files = ", len(files_ZZ[0][1]) + len(files_ZZ[1][1]) + len(files_ZZ[2][1]))

########## VVV #########
files_VVV = nanoGetSampleFiles(mcDirectory, 'ZZZ') + \
        nanoGetSampleFiles(mcDirectory, 'WZZ') + \
        nanoGetSampleFiles(mcDirectory, 'WWZ') + \
        nanoGetSampleFiles(mcDirectory, 'WWW')
# print("VVV files = ", len(files_VVV[0][1])+len(files_VVV[1][1])+len(files_VVV[2][1])+len(files_VVV[3][1]))

print("\n------------------------------------------------------------------------------")

# samples['ZHgg'] = {  # 60 files         ---- DONE
#     'name': files_ZHgg[0][1],}

# samples['ZHllHgg'] = { # 9984 files
#     'name': files_ZHllHgg[0][1],}   

# samples['ggZHllHgg'] = { # 9946 files
#     'name': files_ggZHllHgg[0][1],} 

# samples['DY'] = { #253 FILES
#     'name': files_DY[0][1] + files_DY[1][1],}

# samples['top'] = { # 528 files
#     'name': files_top[0][1] + files_top[1][1] + files_top[2][1] + files_top[3][1] + files_top[4][1] + files_top[5][1],}   

# samples['Vg'] = { # 102 files -------------------- DONE 
#     'name': files_Vg[0][1] + files_Vg[1][1],}    

# samples['VgS'] = { # 215 files
#     'name': files_VgS[0][1] + files_VgS[1][1] + files_VgS[2][1],}   

samples['WZ'] = { # 135 files
    'name': files_WZ[0][1] + files_WZ[1][1],}

# samples['ZZ'] = { # 233 files
#     'name': files_ZZ[0][1] + files_ZZ[1][1] + files_ZZ[2][1],}    

# samples['VVV'] = { # 39 files                   DONE 
#     'name': files_VVV[0][1] + files_VVV[1][1] + files_VVV[2][1] + files_VVV[3][1],}

print("Number of samples:", len(samples.keys()))

for sampleName, sample in samples.items():
    print("Sample:", sampleName, "Number of files:", len(sample['name']))

Output_dir = "/eos/user/a/araghav/BDT_trees"

treeName = "Events"
start_time = time.time()

list_of_branches = {
    "mll": mll,
    "lep_pt1": lep_pt1,
    "lep_pt2": lep_pt2,
    "LowestQGLJet_pt1": LowestQGLJet_pt1,
    "LowestQGLJet_pt2": LowestQGLJet_pt2,
    "LowestQGLJet_pt3": LowestQGLJet_pt3,
    "LowestQGLJet_eta1": LowestQGLJet_eta1,
    "LowestQGLJet_eta2": LowestQGLJet_eta2,
    "LowestQGLJet_phi1": LowestQGLJet_phi1,
    "LowestQGLJet_phi2": LowestQGLJet_phi2,
    "LowestQGLJet_mass1": LowestQGLJet_mass1,
    "LowestQGLJet_mass2": LowestQGLJet_mass2,
    "mjj_qgl": mjj_qgl,
    "ptjj_qgl": ptjj_qgl,
    "detajj_qgl": detajj_qgl,
    "drjj_qgl": drjj_qgl,
}


def process_file(job):
    sampleName, inputFile, outputFile = job

    # print(f"Processing sample: {sampleName}, input file: {inputFile}, output file: {outputFile}")
    fin = ROOT.TFile.Open(inputFile)

    if not fin or fin.IsZombie():
        print(f"Error opening input file: {inputFile}")
        return

    tree= fin.Get(treeName)

    if tree is None:
        print(f"Error: Tree {treeName} not found in file: {inputFile}")
        print(f"Available keys in the file: {[key.GetName() for key in fin.GetListOfKeys()]}")
        fin.Close()
        return

    tree.SetBranchStatus("*", 0)  # Disable all branches

    branches_to_enable = [
        "nLepton",
        "nCleanJet",
        "nJet",
        "mll",
        "Lepton_pt",
        "Lepton_eta",
        "Lepton_pdgId",
        "CleanJet_pt",
        "CleanJet_eta",
        "CleanJet_jetIdx",
        "Jet_btagDeepB",
        "CleanJet_mass",
        "CleanJet_phi",
        "Jet_qgl",
    ]
    for branch in branches_to_enable:
        tree.SetBranchStatus(branch, 1)  # Enable only the branches we need

    fout = ROOT.TFile.Open(outputFile, "RECREATE")
    outTree= ROOT.TTree("Events", "Events")

    branch_arrays = {}

    for branchName in list_of_branches:
        branch_arrays[branchName] = array('f',[0.])

        outTree.Branch(branchName,
                         branch_arrays[branchName],
                         f"{branchName}/F")

    nEntries = tree.GetEntries()

    nSelected = 0

    for iEvent in range(nEntries):
        tree.GetEntry(iEvent)

        if not pass_preselection(tree):
            continue
        nSelected  +=1

        for branchName, func in list_of_branches.items():
            branch_arrays[branchName][0] = func(tree)

        outTree.Fill()

    fout.cd()
    outTree.Write()
    fout.Close()
    fin.Close()

    print(f"{os.path.basename(inputFile)} : {nSelected}/{nEntries}")
    
def create_BDT_trees():

    jobs =[]

    for sampleName, sample in samples.items():

        sampleOutputDir = os.path.join(Output_dir, sampleName)

        os.makedirs(sampleOutputDir, exist_ok=True)

        for inputFile in sample['name']:
            outputFile = os.path.join(
                sampleOutputDir, 
                os.path.basename(inputFile)
            )

            jobs.append((sampleName, inputFile, outputFile))

        print("\n Total files  to process for sample", sampleName, " = ",  {len(sample['name'])})

    print(f"\nTotal files to process = {len(jobs)}")

    nWorkers = multiprocessing.cpu_count()
    print(f"Using {nWorkers} workers for parallel processing.")

    # with ProcessPoolExecutor(max_workers=nWorkers) as executor:
        # executor.map(process_file, jobs)
        # list(executor.map(process_file, jobs))
    with ProcessPoolExecutor(max_workers=nWorkers) as executor:

        futures = [executor.submit(process_file, job) for job in jobs]

        for future in   as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print("Worker crashed:", e)

if __name__ == "__main__":
    start_time = time.time()

    create_BDT_trees()
    end_time = time.time()

    elapsed = end_time - start_time
    print("\n" + "="*80)
    print(f"Total execution time: {elapsed:.2f} seconds")
    print(f"                    = {elapsed/60:.2f} minutes")
    print(f"                    = {elapsed/3600:.2f} hours")
    print("="*80)

# end_time = time.time()

# elapsed = end_time - start_time
# print("\n" + "="*80)
# print(f"Total execution time: {elapsed:.2f} seconds")
# print(f"                    = {elapsed/60:.2f} minutes")
# print(f"                    = {elapsed/3600:.2f} hours")
# print("="*80)