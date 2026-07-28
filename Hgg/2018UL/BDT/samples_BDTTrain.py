import os, glob
import inspect
from mkShapesRDF.lib.search_files import SearchFiles
s = SearchFiles()


UseXROOTD = True
redirector = 'root://eoscms.cern.ch/'
# /afs/cern.ch/user/n/ntrevisa/work/latinos/unblinding/CMSSW_10_6_4/src/PlotsConfigurations/Configurations/WH_chargeAsymmetry/WH3l/BDTconfig/Full2018_nAODv4

configurations = os.path.realpath(inspect.getfile(inspect.currentframe())) # this file
configurations = os.path.dirname(configurations) # Full2018_nAODv4
configurations = os.path.dirname(configurations) # BDTconfig
configurations = os.path.dirname(configurations) # WH3l
configurations = os.path.dirname(configurations) # WH_chargeAsymmetry
configurations = os.path.dirname(configurations) # Configurations

# from LatinoAnalysis.Tools.commonTools import getSampleFiles, getBaseW, addSampleWeight, getBaseWnAOD


def nanoGetSampleFiles(path, name):
    _files = s.searchFiles(path, name, redirector=redirector)
    if limitFiles != -1 and len(_files) > limitFiles:
        return [(name, _files[:limitFiles])]
    else:
        return [(name, _files)]

def nanoGetLocalSampleFiles(path, name):
    print ("nanoGetLocalSampleFiles!")
    _files = s.searchFiles(path, name, redirector='')
    if limitFiles != -1 and len(_files) > limitFiles:
        return [(name, _files[:limitFiles])]
    else:
        return [(name, _files)]

def addSampleWeight(samples, sampleName, sampleNameType, weight):
    obj = list(filter(lambda k: k[0] == sampleNameType, samples[sampleName]['name']))[0]
    samples[sampleName]['name'] = list(filter(lambda k: k[0] != sampleNameType, samples[sampleName]['name']))
    if len(obj) > 2:
        samples[sampleName]['name'].append((obj[0], obj[1], obj[2] + '*(' + weight + ')'))
    else:
        samples[sampleName]['name'].append((obj[0], obj[1], '(' + weight + ')' ))

# samples

try:
    len(samples)
except NameError:
    import collections
    samples = collections.OrderedDict()

################################################
################# SKIMS ########################
################################################

mcProduction = 'Summer20UL18_106x_nAODv9_Full2018v9'
mcSteps = 'MCl1loose2018v9__MCCorr2018v9NoJERInHorn__l2tightOR2018v9'

##############################################
###### Tree base directory for the site ######
##############################################

# SITE=os.uname()[1]
# if    'iihe' in SITE: # what is this? iihe?
#   treeBaseDir = '/pnfs/iihe/cms/store/user/xjanssen/HWW2015'
# elif  'cern' in SITE:
#   treeBaseDir = '/eos/cms/store/group/phys_higgs/cmshww/amassiro/HWWNano'

##############################################
###### Tree base directory for the site ######
##############################################

treeBaseDir = '/eos/cms/store/group/phys_higgs/cmshww/amassiro/HWWNano'
limitFiles  = -1  # why on earth would you want to limit the number of files? Debug reason??
# limitFiles  = 1  # why on earth would you want to limit the number of files? Debug reason??

def makeMCDirectory(var=''):
    if var:
        return os.path.join(treeBaseDir, mcProduction, mcSteps.format(var='__' + var))
    else:
        return os.path.join(treeBaseDir, mcProduction, mcSteps.format(var=''))

mcDirectory = makeMCDirectory()

#########################################
############ MC COMMON ##################
#########################################

# SFweight does not include btag weights
mcCommonWeightNoMatch = 'XSWeight*SFweight*METFilter_MC'
mcCommonWeight        = 'XSWeight*SFweight*METFilter_MC*PromptGenLepMatch2l'

###########################################
#############  BACKGROUNDS  ###############
###########################################

################ DY #######################
files = nanoGetSampleFiles(mcDirectory, 'DYJetsToLL_M-10to50_NLO') + \
        nanoGetSampleFiles(mcDirectory, 'DYJetsToLL_M-50')

samples['DY'] = {
    'name': files,
    'weight': mcCommonWeight + '*1',
    'FilesPerJob': 4
}


################# Top ######################
files = nanoGetSampleFiles(mcDirectory, 'TTTo2L2Nu') + \
        nanoGetSampleFiles(mcDirectory, 'ST_s-channel') + \
        nanoGetSampleFiles(mcDirectory, 'ST_t-channel_top') + \
        nanoGetSampleFiles(mcDirectory, 'ST_t-channel_antitop') + \
        nanoGetSampleFiles(mcDirectory, 'ST_tW_antitop') + \
        nanoGetSampleFiles(mcDirectory, 'ST_tW_top')
        
samples['top'] = {
    'name': files,
    'weight': mcCommonWeight,
    'FilesPerJob': 8
}
addSampleWeight(samples, 'top', 'TTTo2L2Nu', 'Top_pTrw')


######## Vg ########

files = nanoGetSampleFiles(mcDirectory, 'Wg_AMCNLOFXFX_01J') + \
        nanoGetSampleFiles(mcDirectory, 'ZGToLLG')

samples['Vg'] = {
    'name': files,
    'weight': mcCommonWeightNoMatch + '*(Gen_ZGstar_mass <= 0)*1',
    'FilesPerJob': 4,
}

######## VgS ########

files = nanoGetSampleFiles(mcDirectory, 'Wg_AMCNLOFXFX_01J') + \
        nanoGetSampleFiles(mcDirectory, 'WZTo3LNu_mllmin0p1') + \
        nanoGetSampleFiles(mcDirectory, 'ZGToLLG')

samples['VgS'] = {
    'name': files,
    'weight': mcCommonWeight + '*1',
    'FilesPerJob': 4,
}
addSampleWeight(samples, 'VgS', 'Wg_AMCNLOFXFX_01J',  '((Gen_ZGstar_mass > 0 && Gen_ZGstar_mass <= 0.1))*(gstarLow*0.94)')
addSampleWeight(samples, 'VgS', 'WZTo3LNu_mllmin0p1', '((Gen_ZGstar_mass > 0.1)*(0.601644*58.59/4.666))*(gstarLow*0.94)')
addSampleWeight(samples, 'VgS', 'ZGToLLG',            '(Gen_ZGstar_mass > 0)')

############ WZ ############

files = nanoGetSampleFiles(mcDirectory, 'WZTo3LNu_mllmin0p1') + \
        nanoGetSampleFiles(mcDirectory, 'WZTo2Q2L_mllmin4p0')

samples['WZ'] = {
    'name': files,
    'weight': mcCommonWeight + ' * (gstarHigh)*1',
    'FilesPerJob': 4
}
addSampleWeight(samples, 'WZ', 'WZTo3LNu_mllmin0p1', '(0.601644*58.59/4.666)')


############ ZZ ############
files = nanoGetSampleFiles(mcDirectory, 'ZZTo2L2Nu') + \
        nanoGetSampleFiles(mcDirectory, 'ZZTo2Q2L_mllmin4p0') + \
        nanoGetSampleFiles(mcDirectory, 'ZZTo4L')

samples['ZZ'] = {
    'name': files,
    'weight': mcCommonWeight + '*1',
    'FilesPerJob': 4
}

########## VVV #########

########## VVV #########
files = nanoGetSampleFiles(mcDirectory, 'ZZZ') + \
        nanoGetSampleFiles(mcDirectory, 'WZZ') + \
        nanoGetSampleFiles(mcDirectory, 'WWZ') + \
        nanoGetSampleFiles(mcDirectory, 'WWW')

samples['VVV'] = {
    'name': files,
    'weight': mcCommonWeight + '*1',
    'FilesPerJob': 4
}


###########################################
#############   SIGNALS  ##################
###########################################

signals = []

signal_path = "/eos/user/a/amassiro/HIG/ZHggPostProc/Summer20UL18_106x_nAODv9_Full2018v9/MCFull2018v9/"

samples['Hgluglu'] = {
    'name':  nanoGetLocalSampleFiles(signal_path, "ZHgg"),
    'weight': "baseW*genWeight*0.8839*0.08187*0.033658*3",
    'FilesPerJob': 1
}
signals.append('Hgluglu')

samples['qqZHgluglu'] = {
    'name': nanoGetLocalSampleFiles(signal_path, 'ZHllHgg'),
    "weight": "baseW*genWeight*0.7612*0.08187*0.033658*3",
    "FilesPerJob": 200,
}
signals.append('qqZHgluglu')


samples['ggZHgluglu'] = {
    'name':  nanoGetLocalSampleFiles(signal_path, 'ggZHllHgg'),
    'weight': "baseW*genWeight*0.1227*0.08187*0.033658*3",
    'FilesPerJob': 200
}
signals.append('ggZHgluglu')

# samples['WH_htt_minus'] = {
#     'name':  nanoGetSampleFiles(mcDirectory, 'HWminusJ_HToTauTau_M125'),
#     'weight': mcCommonWeight,
#     'FilesPerJob': 4
# }
# signals.append('WH_htt_minus')
