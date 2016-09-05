from flask import Flask, render_template, request, send_file, redirect, url_for
from sens_calc import sens_calc
from Naked.toolshed.shell import execute_js
import webbrowser
import os
import numpy as np



app = Flask(__name__)

app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 1



'''
Bands_cbe= {'lmin':(np.array([0.0,0.0,0.0,0.0]),'um'),\
                'lmax':(np.array([0.0,0.0,0.0,0.0]),'um'),\
                'R':(np.array([0.0,0.0,0.0,0.0]),''),\
                'Format':(np.array([0.0,0.0,0.0,0.0]),''),\
                'dQ':(np.array([0.0,0.0,0.0,0.0]),'e-'),\
                'DC':(np.array([0.0,0.0,0.0,0.0]),'e-/s'),\
                'Pitch':(np.array([0.0,0.0,0.0,0.0]),'um'),\
                'Smile_loss':(np.array([0.0,0.0,0.0,0.0]),'pix'),\
                'Pad_loss':(np.array([0.0,0.0,0.0,0.0]),'pix'),\
                'eta_mir_Au':(np.array([0.0,0.0,0.0,0.0]),'3xAu'),\
                'eta_dich':(np.array([0.0,0.0,0.0,0.0]),''),\
                'eta_lvf':(np.array([0.0,0.0,0.0,0.0]),''),\
                'eta_fpa':(np.array([0.0,0.0,0.0,0.0]),''),\
                'T_samp':(np.array([0.0,0.0,0.0,0.0]),'s'),\
                'Nps':(np.array([0.0,0.0,0.0,0.0]),''),\
                ## Corresponds to Npix_0 in the N_eff formula
                ## Irrelevant if Npix_0 is defined below
                ##'nIn':(np.array([788.5,338.7,106.0,55.0]),'nW/m2/sr')
                }

Bands_mev= {'lmin':(np.array([0.0,0.0,0.0,0.0]),'um'),\
                'lmax':(np.array([0.0,0.0,0.0,0.0]),'um'),\
                'R':(np.array([0.0,0.0,0.0,0.0]),''),\
                'Format':(np.array([0.0,0.0,0.0,0.0]),''),\
                'dQ':(np.array([0.0,0.0,0.0,0.0]),'e-'),\
                'DC':(np.array([0.0,0.0,0.0,0.0]),'e-/s'),\
                'Pitch':(np.array([0.0,0.0,0.0,0.0]),'um'),\
                'Smile_loss':(np.array([0.0,0.0,0.0,0.0]),'pix'),\
                'Pad_loss':(np.array([0.0,0.0,0.0,0.0]),'pix'),\
                'eta_mir_Au':(np.array([0.0,0.0,0.0,0.0]),'3xAu'),\
                'eta_dich':(np.array([0.0,0.0,0.0,0.0]),''),\
                'eta_lvf':(np.array([0.0,0.0,0.0,0.0]),''),\
                'eta_fpa':(np.array([0.0,0.0,0.0,0.0]),''),\
                'T_samp':(np.array([0.0,0.0,0.0,0.0]),'s'),\
                'Nps':(np.array([0.0,0.0,0.0,0.0]),''),\
                ## Corresponds to Npix_0 in the N_eff formula
                ## Irrelevant if Npix_0 is defined below
                ##'nIn':(np.array([788.5,338.7,106.0,55.0]),'nW/m2/sr')
                }
'''
Bands_cbe_7= {'lmin':(np.array([0.75,1.25,2.09,2.60]),'um'),\
                'lmax':(np.array([1.25,2.09,3.50,5.00]),'um'),\
                'R':(np.array([40.,40.,40.,150.]),''),\
                'Format':(np.array([2048.,2048.,2048.,2048.]),''),\
                'dQ':(np.array([10.5,10.5,10.5,10.5]),'e-'),\
                'Pitch':(np.array([18.,18.,18.,18.]),'um'),\
                'eta_mir_Ai':(np.array([0.74,0.88,0.94,0.97]),'3xAI'),\
                'eta_mir_Au':(np.array([0.94,0.97,0.97,0.97]),'3xAu'),\
                'eta_dich':(np.array([0.95,0.95,0.95,0.95]),''),\
                'eta_lvf':(np.array([0.75,0.75,0.75,0.75]),''),\
                'eta_fpa':(np.array([0.75,0.75,0.75,0.75]),''),\
                'T_samp':(np.array([1.5,1.5,1.5,1.5]),'s'),\
                'Nps':(np.array([1.7268,1.7268,1.7268,1.7268]),''),\
                ## Corresponds to Npix_0 in the N_eff formula
                ## Irrelevant if Npix_0 is defined below
                'nIn':(np.array([788.5,338.7,106.0,55.0]),'nW/m2/sr')}

Bands_mev_7= {'lmin':(np.array([0.75,1.25,2.09,2.60]),'um'),\
                'lmax':(np.array([1.25,2.09,3.50,5.00]),'um'),\
                'R':(np.array([40.,40.,40.,150.]),''),\
                'Format':(np.array([2048.,2048.,2048.,2048.]),''),\
                'dQ':(np.array([18.0,18.0,15.0,15.0]),'e-'),\
                'Pitch':(np.array([18.,18.,18.,18.]),'um'),\
                'eta_mir_Ai':(np.array([0.74,0.88,0.94,0.97]),'3xAI'),\
                'eta_mir_Au':(np.array([0.88,0.88,0.88,0.88]),'3xAu'),\
                'eta_dich':(np.array([0.95,0.95,0.95,0.95]),''),\
                'eta_lvf':(np.array([0.50,0.50,0.50,0.50]),''),\
                'eta_fpa':(np.array([0.70,0.70,0.70,0.70]),''),\
                'T_samp':(np.array([1.5,1.5,1.5,1.5]),'s'),\
                'Nps':(np.array([4.01,4.15,4.54,5.05]),''),\
                 ## Corresponds to Npix_0 in the N_eff formula
                 ## Irrelevant if Npix_0 is defined below
                'nIn':(np.array([788.5,338.7,106.0,55.0]),'nW/m2/sr')}

Bands_cbe_8= {'lmin':(np.array([0.75,1.25,2.09,2.60]),'um'),\
                'lmax':(np.array([1.25,2.09,3.50,5.00]),'um'),\
                'R':(np.array([40.,40.,40.,150.]),''),\
                'Format':(np.array([2048.,2048.,2048.,2048.]),''),\
                'dQ':(np.array([10.5,10.5,10.5,10.5]),'e-'),\
                'Pitch':(np.array([18.,18.,18.,18.]),'um'),\
                'eta_mir_Au':(np.array([0.94,0.97,0.97,0.97]),'3xAu'),\
                'eta_dich':(np.array([0.95,0.95,0.95,0.95]),''),\
                'eta_lvf':(np.array([0.75,0.75,0.75,0.75]),''),\
                'eta_fpa':(np.array([0.75,0.75,0.75,0.75]),''),\
                'T_samp':(np.array([1.5,1.5,1.5,1.5]),'s'),\
                ##'Nps':(np.array([1.7268,1.7268,1.7268,1.7268]),''),\
                ## Corresponds to Npix_0 in the N_eff formula
                ## Irrelevant if Npix_0 is defined below
                'nIn':(np.array([788.5,338.7,106.0,55.0]),'nW/m2/sr')}

Bands_mev_8= {'lmin':(np.array([0.75,1.25,2.09,2.60]),'um'),\
                'lmax':(np.array([1.25,2.09,3.50,5.00]),'um'),\
                'R':(np.array([40.,40.,40.,150.]),''),\
                'Format':(np.array([2048.,2048.,2048.,2048.]),''),\
                'dQ':(np.array([18.,18.,18.,18.]),'e-'),\
                'Pitch':(np.array([18.,18.,18.,18.]),'um'),\
                'eta_mir_Au':(np.array([0.88,0.88,0.88,0.88]),'3xAu'),\
                'eta_dich':(np.array([0.95,0.95,0.95,0.95]),''),\
                'eta_lvf':(np.array([0.50,0.50,0.50,0.50]),''),\
                'eta_fpa':(np.array([0.70,0.70,0.70,0.70]),''),\
                'T_samp':(np.array([1.5,1.5,1.5,1.5]),'s'),\
                'nIn':(np.array([788.5,338.7,106.0,55.0]),'nW/m2/sr')}

Bands_cbe_thresv1_8= {'lmin':(np.array([0.75,1.73]),'um'),\
                'lmax':(np.array([1.73,4.00]),'um'),\
                'R':(np.array([30.,30.]),''),\
                'Format':(np.array([2048.,2048.]),''),\
                'dQ':(np.array([10.5,10.5]),'e-'),\
                'Pitch':(np.array([18.,18.]),'um'),\
                'eta_mir_Au':(np.array([0.94,0.97]),'4xAu'),\
                'eta_dich':(np.array([0.95,0.95]),''),\
                'eta_lvf':(np.array([0.75,0.75]),''),\
                'eta_fpa':(np.array([0.75,0.75]),''),\
                'T_samp':(np.array([1.5,1.5]),'s'),\
                'nIn':(np.array([627.9,131.4]),'nW/m2/sr')}

Bands_mev_thresv1_8= {'lmin':(np.array([0.75,1.73]),'um'),\
                'lmax':(np.array([1.73,4.00]),'um'),\
                'R':(np.array([30.,30.]),''),\
                'Format':(np.array([2048.,2048.]),''),\
                'dQ':(np.array([18.0,15.0]),'e-'),\
                'Pitch':(np.array([18.,18.]),'um'),\
                'eta_mir_Au':(np.array([0.88,0.88]),'4xAu'),\
                'eta_dich':(np.array([0.95,0.95]),''),\
                'eta_lvf':(np.array([0.50,0.50]),''),\
                'eta_fpa':(np.array([0.70,0.70]),''),\
                'T_samp':(np.array([1.5,1.5]),'s'),\
                'nIn':(np.array([627.9,131.4]),'nW/m2/sr')}

Bands_cbe_thresv2_8= {'lmin':(np.array([0.75,1.25,2.09,2.60]),'um'),\
                'lmax':(np.array([1.25,2.09,3.50,5.00]),'um'),\
                'R':(np.array([40.,40.,40.,150.]),''),\
                'Format':(np.array([1448.,1448.,1448.,1448.]),''),\
                'dQ':(np.array([10.5,10.5,10.5,10.5]),'e-'),\
                'Pitch':(np.array([18.,18.,18.,18.]),'um'),\
                'eta_mir_Au':(np.array([0.94,0.97,0.97,0.97]),'3xAu'),\
                'eta_dich':(np.array([0.95,0.95,0.95,0.95]),''),\
                'eta_lvf':(np.array([0.75,0.75,0.75,0.75]),''),\
                'eta_fpa':(np.array([0.75,0.75,0.75,0.75]),''),\
                'T_samp':(np.array([1.5,1.5,1.5,1.5]),'s'),\
                ##'Nps':(np.array([1.7268,1.7268,1.7268,1.7268]),''),\
                ## Corresponds to Npix_0 in the N_eff formula
                ## Irrelevant if Npix_0 is defined below
                'nIn':(np.array([788.5,338.7,106.0,55.0]),'nW/m2/sr')}

Bands_mev_thresv2_8= {'lmin':(np.array([0.75,1.25,2.09,2.60]),'um'),\
                'lmax':(np.array([1.25,2.09,3.50,5.00]),'um'),\
                'R':(np.array([40.,40.,40.,150.]),''),\
                'Format':(np.array([1448.,1448.,1448.,1448.]),''),\
                'dQ':(np.array([18.0,18.0,15.0,15.0]),'e-'),\
                'Pitch':(np.array([18.,18.,18.,18.]),'um'),\
                'eta_mir_Au':(np.array([0.88,0.88,0.88,0.88]),'3xAu'),\
                'eta_dich':(np.array([0.95,0.95,0.95,0.95]),''),\
                'eta_lvf':(np.array([0.50,0.50,0.50,0.50]),''),\
                'eta_fpa':(np.array([0.70,0.70,0.70,0.70]),''),\
                'T_samp':(np.array([1.5,1.5,1.5,1.5]),'s'),\
                ##'Nps':(np.array([1.7268,1.7268,1.7268,1.7268]),''),\
                ## Corresponds to Npix_0 in the N_eff formula
                ## Irrelevant if Npix_0 is defined below
                'nIn':(np.array([788.5,338.7,106.0,55.0]),'nW/m2/sr')}

Bands_cbe_12= {'lmin':(np.array([0.75,1.32,2.34,4.12]),'um'),\
                'lmax':(np.array([1.32,2.34,4.12,4.83]),'um'),\
                'R':(np.array([41.5,41.5,41.5,150.]),''),\
                'Format':(np.array([2048.,2048.,2048.,2048.]),''),\
                'dQ':(np.array([10.5,10.5,10.5,10.5]),'e-'),\
                'Pitch':(np.array([18.,18.,18.,18.]),'um'),\
                'eta_mir_Au':(np.array([0.94,0.97,0.97,0.97]),'3xAu'),\
                'eta_dich':(np.array([0.95,0.95,0.95,0.95]),''),\
                'eta_lvf':(np.array([0.75,0.75,0.75,0.75]),''),\
                'eta_fpa':(np.array([0.75,0.75,0.75,0.75]),''),\
                'T_samp':(np.array([1.5,1.5,1.5,1.5]),'s'),\
                ##'Nps':(np.array([1.7268,1.7268,1.7268,1.7268]),''),\
                ## Corresponds to Npix_0 in the N_eff formula
                ## Irrelevant if Npix_0 is defined below
                ##'nIn':(np.array([788.5,338.7,106.0,55.0]),'nW/m2/sr')
                }

Bands_mev_12= {'lmin':(np.array([0.75,1.32,2.34,4.12]),'um'),\
                'lmax':(np.array([1.32,2.34,4.12,4.83]),'um'),\
                'R':(np.array([41.5,41.5,41.5,150.]),''),\
                'Format':(np.array([2048.,2048.,2048.,2048.]),''),\
                'dQ':(np.array([15.0,15.0,15.0,15.0]),'e-'),\
                'Pitch':(np.array([18.,18.,18.,18.]),'um'),\
                'eta_mir_Au':(np.array([0.88,0.88,0.88,0.88]),'3xAu'),\
                'eta_dich':(np.array([0.95,0.95,0.95,0.95]),''),\
                'eta_lvf':(np.array([0.50,0.50,0.50,0.50]),''),\
                'eta_fpa':(np.array([0.70,0.70,0.70,0.70]),''),\
                'T_samp':(np.array([1.5,1.5,1.5,1.5]),'s'),\
                ##'Nps':(np.array([1.7268,1.7268,1.7268,1.7268]),''),\
                ## Corresponds to Npix_0 in the N_eff formula
                ## Irrelevant if Npix_0 is defined below
                ##'nIn':(np.array([788.5,338.7,106.0,55.0]),'nW/m2/sr')
                }

Bands_cbe_12_thres = {'lmin':(np.array([0.75,1.32,2.34,4.12]),'um'),\
                'lmax':(np.array([1.32,2.34,4.12,4.83]),'um'),\
                'R':(np.array([41.5,41.5,41.5,150.]),''),\
                'Format':(np.array([2048.,2048.,2048.,2048.]),''),\
                'dQ':(np.array([10.5,10.5,10.5,10.5]),'e-'),\
                'Pitch':(np.array([18.,18.,18.,18.]),'um'),\
                'eta_mir_Au':(np.array([0.94,0.97,0.97,0.97]),'3xAu'),\
                'eta_dich':(np.array([0.95,0.95,0.95,0.95]),''),\
                'eta_lvf':(np.array([0.75,0.75,0.75,0.75]),''),\
                'eta_fpa':(np.array([0.75,0.75,0.75,0.75]),''),\
                'T_samp':(np.array([1.5,1.5,1.5,1.5]),'s'),\
                ##'Nps':(np.array([1.7268,1.7268,1.7268,1.7268]),''),\
                ## Corresponds to Npix_0 in the N_eff formula
                ## Irrelevant if Npix_0 is defined below
                ##'nIn':(np.array([788.5,338.7,106.0,55.0]),'nW/m2/sr')
                }

Bands_mev_12_thres = {'lmin':(np.array([0.75,1.32,2.34,4.12]),'um'),\
                'lmax':(np.array([1.32,2.34,4.12,4.83]),'um'),\
                'R':(np.array([41.5,41.5,41.5,150.]),''),\
                'Format':(np.array([2048.,2048.,2048.,2048.]),''),\
                'dQ':(np.array([15.0,15.0,15.0,15.0]),'e-'),\
                'Pitch':(np.array([18.,18.,18.,18.]),'um'),\
                'eta_mir_Au':(np.array([0.88,0.88,0.88,0.88]),'3xAu'),\
                'eta_dich':(np.array([0.95,0.95,0.95,0.95]),''),\
                'eta_lvf':(np.array([0.50,0.50,0.50,0.50]),''),\
                'eta_fpa':(np.array([0.70,0.70,0.70,0.70]),''),\
                'T_samp':(np.array([1.5,1.5,1.5,1.5]),'s'),\
                ##'Nps':(np.array([1.7268,1.7268,1.7268,1.7268]),''),\
                ## Corresponds to Npix_0 in the N_eff formula
                ## Irrelevant if Npix_0 is defined below
                ##'nIn':(np.array([788.5,338.7,106.0,55.0]),'nW/m2/sr')
                }

Bands_cbe_13= {'lmin':(np.array([0.75,1.32,2.34,4.12]),'um'),\
                'lmax':(np.array([1.32,2.34,4.12,4.83]),'um'),\
                'R':(np.array([41.5,41.5,41.5,150.]),''),\
                'Format':(np.array([2048.,2048.,2048.,2048.]),''),\
                'dQ':(np.array([10.5,10.5,10.5,10.5]),'e-'),\
                'Pitch':(np.array([18.,18.,18.,18.]),'um'),\
                'Smile_loss':(np.array([76.,76.,76.,76.]),'pix'),\
                'Pad_loss':(np.array([47.,47.,47.,47.]),'pix'),\
                'eta_mir_Au':(np.array([0.94,0.97,0.97,0.97]),'3xAu'),\
                'eta_dich':(np.array([0.95,0.95,0.95,0.95]),''),\
                'eta_lvf':(np.array([0.85,0.85,0.85,0.85]),''),\
                'eta_fpa':(np.array([0.75,0.75,0.75,0.75]),''),\
                'T_samp':(np.array([1.5,1.5,1.5,1.5]),'s'),\
                ##'Nps':(np.array([1.7268,1.7268,1.7268,1.7268]),''),\
                ## Corresponds to Npix_0 in the N_eff formula
                ## Irrelevant if Npix_0 is defined below
                ##'nIn':(np.array([788.5,338.7,106.0,55.0]),'nW/m2/sr')
                }

Bands_mev_13= {'lmin':(np.array([0.75,1.32,2.34,4.12]),'um'),\
                'lmax':(np.array([1.32,2.34,4.12,4.83]),'um'),\
                'R':(np.array([41.5,41.5,41.5,150.]),''),\
                'Format':(np.array([2048.,2048.,2048.,2048.]),''),\
                'dQ':(np.array([10.5,10.5,10.5,10.5]),'e-'),\
                'Pitch':(np.array([18.,18.,18.,18.]),'um'),\
                'Smile_loss':(np.array([76.,76.,76.,76.]),'pix'),\
                'Pad_loss':(np.array([47.,47.,47.,47.]),'pix'),\
                'eta_mir_Au':(np.array([0.88,0.88,0.88,0.88]),'3xAu'),\
                'eta_dich':(np.array([0.95,0.95,0.95,0.95]),''),\
                'eta_lvf':(np.array([0.80,0.80,0.80,0.80]),''),\
                'eta_fpa':(np.array([0.70,0.70,0.70,0.70]),''),\
                'T_samp':(np.array([1.5,1.5,1.5,1.5]),'s'),\
                ##'Nps':(np.array([1.7268,1.7268,1.7268,1.7268]),''),\
                ## Corresponds to Npix_0 in the N_eff formula
                ## Irrelevant if Npix_0 is defined below
                ##'nIn':(np.array([788.5,338.7,106.0,55.0]),'nW/m2/sr')
                }

Bands_cbe_14 = {'lmin':(np.array([0.75,1.32,2.34,4.12]),'um'),\
                'lmax':(np.array([1.32,2.34,4.12,4.83]),'um'),\
                'R':(np.array([41.5,41.5,41.5,150.]),''),\
                'Format':(np.array([2048.,2048.,2048.,2048.]),''),\
                'dQ':(np.array([15.0,15.0,15.0,15.0]),'e-'),\
                'DC':(np.array([0.05,0.05,0.05,0.05]),'e-/s'),\
                'Pitch':(np.array([18.,18.,18.,18.]),'um'),\
                'Smile_loss':(np.array([76.,76.,76.,76.]),'pix'),\
                'Pad_loss':(np.array([47.,47.,47.,47.]),'pix'),\
                'eta_mir_Au':(np.array([0.88,0.88,0.88,0.88]),'3xAu'),\
                'eta_dich':(np.array([0.95,0.95,0.95,0.95]),''),\
                'eta_lvf':(np.array([0.80,0.80,0.80,0.80]),''),\
                'eta_fpa':(np.array([0.70,0.70,0.70,0.70]),''),\
                'T_samp':(np.array([1.5,1.5,1.5,1.5]),'s'),\
                ##'Nps':(np.array([1.7268,1.7268,1.7268,1.7268]),''),\
                ## Corresponds to Npix_0 in the N_eff formula
                ## Irrelevant if Npix_0 is defined below
                ##'nIn':(np.array([788.5,338.7,106.0,55.0]),'nW/m2/sr')
                }

Bands_mev_14 = {'lmin':(np.array([0.75,1.32,2.34,4.12]),'um'),\
                'lmax':(np.array([1.32,2.34,4.12,4.83]),'um'),\
                'R':(np.array([41.5,41.5,41.5,150.]),''),\
                'Format':(np.array([2048.,2048.,2048.,2048.]),''),\
                'dQ':(np.array([10.5,10.5,10.5,10.5]),'e-'),\
                'DC':(np.array([0.01,0.01,0.01,0.01]),'e-/s'),\
                'Pitch':(np.array([18.,18.,18.,18.]),'um'),\
                'Smile_loss':(np.array([76.,76.,76.,76.]),'pix'),\
                'Pad_loss':(np.array([47.,47.,47.,47.]),'pix'),\
                'eta_mir_Au':(np.array([0.94,0.97,0.97,0.97]),'3xAu'),\
                'eta_dich':(np.array([0.95,0.95,0.95,0.95]),''),\
                'eta_lvf':(np.array([0.85,0.85,0.85,0.85]),''),\
                'eta_fpa':(np.array([0.75,0.75,0.75,0.75]),''),\
                'T_samp':(np.array([1.5,1.5,1.5,1.5]),'s'),\
                ##'Nps':(np.array([1.7268,1.7268,1.7268,1.7268]),''),\
                ## Corresponds to Npix_0 in the N_eff formula
                ## Irrelevant if Npix_0 is defined below
                ##'nIn':(np.array([788.5,338.7,106.0,55.0]),'nW/m2/sr')
                }

Bands_cbe_16 = {'lmin':(np.array([0.75,1.33,2.36,4.18]),'um'),\
                'lmax':(np.array([1.33,2.36,4.18,5.00]),'um'),\
                'R':(np.array([41.4,41.4,41.4,135.]),''),\
                'Format':(np.array([2048.,2048.,2048.,2048.]),''),\
                'dQ':(np.array([10.5,10.5,10.5,10.5]),'e-'),\
                'DC':(np.array([0.01,0.01,0.03,0.03]),'e-/s'),\
                'Pitch':(np.array([18.,18.,18.,18.]),'um'),\
                'Smile_loss':(np.array([76.,76.,76.,76.]),'pix'),\
                'Pad_loss':(np.array([47.,47.,47.,47.]),'pix'),\
                'eta_mir_Au':(np.array([0.94,0.97,0.97,0.97]),'3xAu'),\
                'eta_dich':(np.array([0.95,0.95,0.95,0.95]),''),\
                'eta_lvf':(np.array([0.90,0.80,0.80,0.70]),''),\
                'eta_fpa':(np.array([0.75,0.75,0.75,0.75]),''),\
                'T_samp':(np.array([1.5,1.5,1.5,1.5]),'s'),\
                'Nps':(np.array([3.25,3.25,3.25,3.25]),''),\
                ## Corresponds to Npix_0 in the N_eff formula
                ## Irrelevant if Npix_0 is defined below
                ##'nIn':(np.array([788.5,338.7,106.0,55.0]),'nW/m2/sr')
                }

Bands_mev_16 = {'lmin':(np.array([0.75,1.33,2.36,4.18]),'um'),\
                'lmax':(np.array([1.33,2.36,4.18,5.00]),'um'),\
                'R':(np.array([41.4,41.4,41.4,135.]),''),\
                'Format':(np.array([2048.,2048.,2048.,2048.]),''),\
                'dQ':(np.array([15.0,15.0,15.0,15.0]),'e-'),\
                'DC':(np.array([0.05,0.05,0.05,0.05]),'e-/s'),\
                'Pitch':(np.array([18.,18.,18.,18.]),'um'),\
                'Smile_loss':(np.array([76.,76.,76.,76.]),'pix'),\
                'Pad_loss':(np.array([47.,47.,47.,47.]),'pix'),\
                'eta_mir_Au':(np.array([0.88,0.88,0.88,0.88]),'3xAu'),\
                'eta_dich':(np.array([0.95,0.95,0.95,0.95]),''),\
                'eta_lvf':(np.array([0.80,0.75,0.75,0.65]),''),\
                'eta_fpa':(np.array([0.70,0.70,0.70,0.70]),''),\
                'T_samp':(np.array([1.5,1.5,1.5,1.5]),'s'),\
                'Nps':(np.array([7.0,7.0,7.0,7.0]),''),\
                ## Corresponds to Npix_0 in the N_eff formula
                ## Irrelevant if Npix_0 is defined below
                ##'nIn':(np.array([788.5,338.7,106.0,55.0]),'nW/m2/sr')
                }

IV_CBE = {}
IV_MEV = {}
mode = {}
DERIVED_CBE = {}
DERIVED_MEV = {}
version_dict = {}



#using GET
#@app.route('/')
#def index():
	#return "Method used: %s" %request.method
#	return render_template("gui.html")
'''
#using GET or POST
@app.route('/post', methods=['GET', 'POST'])
def post():
	if request.method == 'POST':
		return "you are using post"
	else:
		return "you are using GET"
'''

@app.route('/')
def advanced():
	mode['mode'] = 'advanced'
	version = 'v16'
	version_cap = version + '_baseline_cbe'
	version_req = version + '_baseline_mev'        
	calc = sens_calc(version_cap=version_cap, version_req=version_req)
	inst_cap, inst_req, sens_cap, sens_req, ZL_fac_cap, ZL_fac_req = calc.draw()

	TA_form_cbe = inst_cap['Telescope Aperture (cm)'][0]
	PJ_form_cbe = inst_cap['Pointing Jitter (arcsec)'][0]
	ML_form_cbe = inst_cap['Mission Lifetime (years)'][0]
	LSST_form_cbe = inst_cap['Large Step Slew Time (s)'][0]
	SDST_form_cbe = inst_cap['Small Dither Slew Time (s)'][0]
	TDT_form_cbe = inst_cap['Telemetry Downlink Time (s/orbit)'][0]
	SAADP_form_cbe = inst_cap['South Atlantic Anomaly Down Period (s/orbit)'][0]
	b12rn_form_cbe = inst_cap['Bands']['dQ'][0][0]
	b34rn_form_cbe = inst_cap['Bands']['dQ'][0][2]
	b13srp_form_cbe = inst_cap['Bands']['R'][0][0]
	b4srp_form_cbe = inst_cap['Bands']['R'][0][3]
	asi_form_cbe = inst_cap['Bands']['T_samp'][0][0]
	TOE_form_cbe = sens_cap['der_char']['eta_tot'][0][0]
	ps_form_cbe = sens_cap['der_char']['th_pix'][0][0]
	zi_form_cbe = ZL_fac_cap
	Asfet_form_cbe = sens_cap['der_char']['t_int_sh'][0]
	Dfet_form_cbe = sens_cap['der_char']['t_int_dp'][0]
	Enopfop_form_cbe = sens_cap['der_char']['Neff'][0][0]
	csf_form_cbe = inst_cap['Channel sampling'][0]
	dfa_form_cbe = inst_cap['Deep field area (sq degrees)'][0]
	noa_form_cbe = inst_cap['nbands']

	TA_form_mev = inst_req['Telescope Aperture (cm)'][0]
	PJ_form_mev = inst_req['Pointing Jitter (arcsec)'][0]
	ML_form_mev = inst_req['Mission Lifetime (years)'][0]
	LSST_form_mev = inst_req['Large Step Slew Time (s)'][0]
	SDST_form_mev = inst_req['Small Dither Slew Time (s)'][0]
	TDT_form_mev = inst_req['Telemetry Downlink Time (s/orbit)'][0]
	SAADP_form_mev = inst_req['South Atlantic Anomaly Down Period (s/orbit)'][0]
	b12rn_form_mev = inst_req['Bands']['dQ'][0][0]
	b34rn_form_mev = inst_req['Bands']['dQ'][0][2]
	b13srp_form_mev = inst_req['Bands']['R'][0][0]
	b4srp_form_mev = inst_req['Bands']['R'][0][3]
	asi_form_mev = inst_req['Bands']['T_samp'][0][0]
	TOE_form_mev = sens_req['der_char']['eta_tot'][0][0]
	ps_form_mev = sens_req['der_char']['th_pix'][0][0]
	zi_form_mev = ZL_fac_req
	Asfet_form_mev = sens_req['der_char']['t_int_sh'][0]
	Dfet_form_mev = sens_req['der_char']['t_int_dp'][0]
	Enopfop_form_mev = sens_req['der_char']['Neff'][0][0]
	csf_form_mev = inst_req['Channel sampling'][0]
	dfa_form_mev = inst_req['Deep field area (sq degrees)'][0]
	noa_form_mev = inst_req['nbands']


	#print ps_form_cbe, ps_form_mev #array with same values
	#print TOE_form_cbe, TOE_form_mev #array with different values


	version_dict['version_cap'] = version_cap
	version_dict['version_req'] = version_req
	
	return render_template("table_advanced.html", TA_form_cbe=TA_form_cbe, PJ_form_cbe=PJ_form_cbe, \
		ML_form_cbe=ML_form_cbe, \
		LSST_form_cbe=LSST_form_cbe, SDST_form_cbe=SDST_form_cbe, \
		TDT_form_cbe=TDT_form_cbe, SAADP_form_cbe=SAADP_form_cbe, b12rn_form_cbe=b12rn_form_cbe, b34rn_form_cbe=b34rn_form_cbe, \
		b13srp_form_cbe=b13srp_form_cbe, b4srp_form_cbe=b4srp_form_cbe, asi_form_cbe=asi_form_cbe, TOE_form_cbe=TOE_form_cbe, \
		ps_form_cbe=ps_form_cbe, zi_form_cbe=zi_form_cbe, Asfet_form_cbe=Asfet_form_cbe, Dfet_form_cbe=Dfet_form_cbe, \
		Enopfop_form_cbe=Enopfop_form_cbe, csf_form_cbe=csf_form_cbe, dfa_form_cbe=dfa_form_cbe, noa_form_cbe=noa_form_cbe, \
		TA_form_mev=TA_form_mev, PJ_form_mev=PJ_form_mev, ML_form_mev=ML_form_mev, LSST_form_mev=LSST_form_mev, SDST_form_mev=SDST_form_mev, \
		TDT_form_mev=TDT_form_mev, SAADP_form_mev=SAADP_form_mev, b12rn_form_mev=b12rn_form_mev, \
		b34rn_form_mev=b34rn_form_mev, b13srp_form_mev=b13srp_form_mev, b4srp_form_mev=b4srp_form_mev, asi_form_mev=asi_form_mev, \
		TOE_form_mev=TOE_form_mev, ps_form_mev=ps_form_mev, zi_form_mev=zi_form_mev, Asfet_form_mev=Asfet_form_mev, \
		Dfet_form_mev=Dfet_form_mev, Enopfop_form_mev=Enopfop_form_mev, csf_form_mev=csf_form_mev, dfa_form_mev=dfa_form_mev, \
		noa_form_mev=noa_form_mev)

'''
@app.route('/gui')
def gui():
	food = ["Cheese", "Tuna", "Chicken"]
	return render_template("gui.html", food=food)
'''

@app.route('/v7')
def v7_link():
	#refresh = execute_js('refresh.js')
	version = 'v7'
	version_cap = version + '_capability'
	version_req = version + '_required'        
	calc = sens_calc(version_cap=version_cap, version_req=version_req)
	inst_cap, inst_req = calc.draw()

	TA_form_cbe = inst_cap['Telescope Aperture (cm)'][0]
	PJ_form_cbe = inst_cap['Pointing Jitter (arcsec)'][0]
	ML_form_cbe = inst_cap['Mission Lifetime (years)'][0]
	LSST_form_cbe = inst_cap['Large Step Slew Time (s)'][0]
	SDST_form_cbe = inst_cap['Small Dither Slew Time (s)'][0]
	TDT_form_cbe = inst_cap['Telemetry Downlink Time (s/orbit)'][0]
	SAADP_form_cbe = inst_cap['South Atlantic Anomaly Down Period (s/orbit)'][0]
	b12rn_form_cbe = inst_cap['Bands']['dQ'][0][0]
	b34rn_form_cbe = inst_cap['Bands']['dQ'][0][2]
	b13srp_form_cbe = inst_cap['Bands']['R'][0][0]
	b4srp_form_cbe = inst_cap['Bands']['R'][0][3]
	asi_form_cbe = inst_cap['Bands']['T_samp'][0][0]

	TA_form_mev = inst_req['Telescope Aperture (cm)'][0]
	PJ_form_mev = inst_req['Pointing Jitter (arcsec)'][0]
	ML_form_mev = inst_req['Mission Lifetime (years)'][0]
	LSST_form_mev = inst_req['Large Step Slew Time (s)'][0]
	SDST_form_mev = inst_req['Small Dither Slew Time (s)'][0]
	TDT_form_mev = inst_req['Telemetry Downlink Time (s/orbit)'][0]
	SAADP_form_mev = inst_req['South Atlantic Anomaly Down Period (s/orbit)'][0]
	b12rn_form_mev = inst_req['Bands']['dQ'][0][0]
	b34rn_form_mev = inst_req['Bands']['dQ'][0][2]
	b13srp_form_mev = inst_req['Bands']['R'][0][0]
	b4srp_form_mev = inst_req['Bands']['R'][0][3]
	asi_form_mev = inst_req['Bands']['T_samp'][0][0]

	version_dict['version_cap'] = version_cap
	version_dict['version_req'] = version_req
	
	return render_template("table_advanced.html", TA_form_cbe=TA_form_cbe, PJ_form_cbe=PJ_form_cbe, \
		ML_form_cbe=ML_form_cbe, \
		LSST_form_cbe=LSST_form_cbe, SDST_form_cbe=SDST_form_cbe, \
		TDT_form_cbe=TDT_form_cbe, SAADP_form_cbe=SAADP_form_cbe, b12rn_form_cbe=b12rn_form_cbe, b34rn_form_cbe=b34rn_form_cbe, \
		b13srp_form_cbe=b13srp_form_cbe, b4srp_form_cbe=b4srp_form_cbe, asi_form_cbe=asi_form_cbe, \
		TA_form_mev=TA_form_mev, PJ_form_mev=PJ_form_mev, \
		ML_form_mev=ML_form_mev, LSST_form_mev=LSST_form_mev, SDST_form_mev=SDST_form_mev, \
		TDT_form_mev=TDT_form_mev, SAADP_form_mev=SAADP_form_mev, b12rn_form_mev=b12rn_form_mev, \
		b34rn_form_mev=b34rn_form_mev, b13srp_form_mev=b13srp_form_mev, b4srp_form_mev=b4srp_form_mev, asi_form_mev=asi_form_mev)

@app.route('/v8')
def v8_link():
	version = 'v8'
	version_cap = version + '_baseline_cap'
	version_req = version + '_baseline_req'        
	calc = sens_calc(version_cap=version_cap, version_req=version_req)
	inst_cap, inst_req = calc.draw()

	TA_form_cbe = inst_cap['Telescope Aperture (cm)'][0]
	PJ_form_cbe = inst_cap['Pointing Jitter (arcsec)'][0]
	ML_form_cbe = inst_cap['Mission Lifetime (years)'][0]
	LSST_form_cbe = inst_cap['Large Step Slew Time (s)'][0]
	SDST_form_cbe = inst_cap['Small Dither Slew Time (s)'][0]
	TDT_form_cbe = inst_cap['Telemetry Downlink Time (s/orbit)'][0]
	SAADP_form_cbe = inst_cap['South Atlantic Anomaly Down Period (s/orbit)'][0]
	b12rn_form_cbe = inst_cap['Bands']['dQ'][0][0]
	b34rn_form_cbe = inst_cap['Bands']['dQ'][0][2]
	b13srp_form_cbe = inst_cap['Bands']['R'][0][0]
	b4srp_form_cbe = inst_cap['Bands']['R'][0][3]
	asi_form_cbe = inst_cap['Bands']['T_samp'][0][0]

	TA_form_mev = inst_req['Telescope Aperture (cm)'][0]
	PJ_form_mev = inst_req['Pointing Jitter (arcsec)'][0]
	ML_form_mev = inst_req['Mission Lifetime (years)'][0]
	LSST_form_mev = inst_req['Large Step Slew Time (s)'][0]
	SDST_form_mev = inst_req['Small Dither Slew Time (s)'][0]
	TDT_form_mev = inst_req['Telemetry Downlink Time (s/orbit)'][0]
	SAADP_form_mev = inst_req['South Atlantic Anomaly Down Period (s/orbit)'][0]
	b12rn_form_mev = inst_req['Bands']['dQ'][0][0]
	b34rn_form_mev = inst_req['Bands']['dQ'][0][2]
	b13srp_form_mev = inst_req['Bands']['R'][0][0]
	b4srp_form_mev = inst_req['Bands']['R'][0][3]
	asi_form_mev = inst_req['Bands']['T_samp'][0][0]

	version_dict['version_cap'] = version_cap
	version_dict['version_req'] = version_req
	
	return render_template("table_advanced.html", TA_form_cbe=TA_form_cbe, PJ_form_cbe=PJ_form_cbe, \
		ML_form_cbe=ML_form_cbe, \
		LSST_form_cbe=LSST_form_cbe, SDST_form_cbe=SDST_form_cbe, \
		TDT_form_cbe=TDT_form_cbe, SAADP_form_cbe=SAADP_form_cbe, b12rn_form_cbe=b12rn_form_cbe, b34rn_form_cbe=b34rn_form_cbe, \
		b13srp_form_cbe=b13srp_form_cbe, b4srp_form_cbe=b4srp_form_cbe, asi_form_cbe=asi_form_cbe, \
		TA_form_mev=TA_form_mev, PJ_form_mev=PJ_form_mev, \
		ML_form_mev=ML_form_mev, LSST_form_mev=LSST_form_mev, SDST_form_mev=SDST_form_mev, \
		TDT_form_mev=TDT_form_mev, SAADP_form_mev=SAADP_form_mev, b12rn_form_mev=b12rn_form_mev, \
		b34rn_form_mev=b34rn_form_mev, b13srp_form_mev=b13srp_form_mev, b4srp_form_mev=b4srp_form_mev, asi_form_mev=asi_form_mev)
	
@app.route('/v8_thresv1')
def v8_th1_link():
	version = 'v8_thresv1'
	version_cap = version + '_cap'
	version_req = version + '_req'        
	calc = sens_calc(version_cap=version_cap, version_req=version_req)
	inst_cap, inst_req = calc.draw()

	TA_form_cbe = inst_cap['Telescope Aperture (cm)'][0]
	PJ_form_cbe = inst_cap['Pointing Jitter (arcsec)'][0]
	ML_form_cbe = inst_cap['Mission Lifetime (years)'][0]
	LSST_form_cbe = inst_cap['Large Step Slew Time (s)'][0]
	SDST_form_cbe = inst_cap['Small Dither Slew Time (s)'][0]
	TDT_form_cbe = inst_cap['Telemetry Downlink Time (s/orbit)'][0]
	SAADP_form_cbe = inst_cap['South Atlantic Anomaly Down Period (s/orbit)'][0]
	b12rn_form_cbe = inst_cap['Bands']['dQ'][0][0]
	b34rn_form_cbe = inst_cap['Bands']['dQ'][0][2]
	b13srp_form_cbe = inst_cap['Bands']['R'][0][0]
	b4srp_form_cbe = inst_cap['Bands']['R'][0][3]
	asi_form_cbe = inst_cap['Bands']['T_samp'][0][0]

	TA_form_mev = inst_req['Telescope Aperture (cm)'][0]
	PJ_form_mev = inst_req['Pointing Jitter (arcsec)'][0]
	ML_form_mev = inst_req['Mission Lifetime (years)'][0]
	LSST_form_mev = inst_req['Large Step Slew Time (s)'][0]
	SDST_form_mev = inst_req['Small Dither Slew Time (s)'][0]
	TDT_form_mev = inst_req['Telemetry Downlink Time (s/orbit)'][0]
	SAADP_form_mev = inst_req['South Atlantic Anomaly Down Period (s/orbit)'][0]
	b12rn_form_mev = inst_req['Bands']['dQ'][0][0]
	b34rn_form_mev = inst_req['Bands']['dQ'][0][2]
	b13srp_form_mev = inst_req['Bands']['R'][0][0]
	b4srp_form_mev = inst_req['Bands']['R'][0][3]
	asi_form_mev = inst_req['Bands']['T_samp'][0][0]

	version_dict['version_cap'] = version_cap
	version_dict['version_req'] = version_req
	
	return render_template("table_advanced.html", TA_form_cbe=TA_form_cbe, PJ_form_cbe=PJ_form_cbe, \
		ML_form_cbe=ML_form_cbe, \
		LSST_form_cbe=LSST_form_cbe, SDST_form_cbe=SDST_form_cbe, \
		TDT_form_cbe=TDT_form_cbe, SAADP_form_cbe=SAADP_form_cbe, b12rn_form_cbe=b12rn_form_cbe, b34rn_form_cbe=b34rn_form_cbe, \
		b13srp_form_cbe=b13srp_form_cbe, b4srp_form_cbe=b4srp_form_cbe, asi_form_cbe=asi_form_cbe, \
		TA_form_mev=TA_form_mev, PJ_form_mev=PJ_form_mev, \
		ML_form_mev=ML_form_mev, LSST_form_mev=LSST_form_mev, SDST_form_mev=SDST_form_mev, \
		TDT_form_mev=TDT_form_mev, SAADP_form_mev=SAADP_form_mev, b12rn_form_mev=b12rn_form_mev, \
		b34rn_form_mev=b34rn_form_mev, b13srp_form_mev=b13srp_form_mev, b4srp_form_mev=b4srp_form_mev, asi_form_mev=asi_form_mev)

@app.route('/v8_thresv2')
def v8_th2_link():
	version = 'v8_thresv2'
	version_cap = version + '_cap'
	version_req = version + '_req'        
	calc = sens_calc(version_cap=version_cap, version_req=version_req)
	inst_cap, inst_req = calc.draw()

	TA_form_cbe = inst_cap['Telescope Aperture (cm)'][0]
	PJ_form_cbe = inst_cap['Pointing Jitter (arcsec)'][0]
	ML_form_cbe = inst_cap['Mission Lifetime (years)'][0]
	LSST_form_cbe = inst_cap['Large Step Slew Time (s)'][0]
	SDST_form_cbe = inst_cap['Small Dither Slew Time (s)'][0]
	TDT_form_cbe = inst_cap['Telemetry Downlink Time (s/orbit)'][0]
	SAADP_form_cbe = inst_cap['South Atlantic Anomaly Down Period (s/orbit)'][0]
	b12rn_form_cbe = inst_cap['Bands']['dQ'][0][0]
	b34rn_form_cbe = inst_cap['Bands']['dQ'][0][2]
	b13srp_form_cbe = inst_cap['Bands']['R'][0][0]
	b4srp_form_cbe = inst_cap['Bands']['R'][0][3]
	asi_form_cbe = inst_cap['Bands']['T_samp'][0][0]

	TA_form_mev = inst_req['Telescope Aperture (cm)'][0]
	PJ_form_mev = inst_req['Pointing Jitter (arcsec)'][0]
	ML_form_mev = inst_req['Mission Lifetime (years)'][0]
	LSST_form_mev = inst_req['Large Step Slew Time (s)'][0]
	SDST_form_mev = inst_req['Small Dither Slew Time (s)'][0]
	TDT_form_mev = inst_req['Telemetry Downlink Time (s/orbit)'][0]
	SAADP_form_mev = inst_req['South Atlantic Anomaly Down Period (s/orbit)'][0]
	b12rn_form_mev = inst_req['Bands']['dQ'][0][0]
	b34rn_form_mev = inst_req['Bands']['dQ'][0][2]
	b13srp_form_mev = inst_req['Bands']['R'][0][0]
	b4srp_form_mev = inst_req['Bands']['R'][0][3]
	asi_form_mev = inst_req['Bands']['T_samp'][0][0]

	version_dict['version_cap'] = version_cap
	version_dict['version_req'] = version_req
	
	return render_template("table_advanced.html", TA_form_cbe=TA_form_cbe, PJ_form_cbe=PJ_form_cbe, \
		ML_form_cbe=ML_form_cbe, \
		LSST_form_cbe=LSST_form_cbe, SDST_form_cbe=SDST_form_cbe, \
		TDT_form_cbe=TDT_form_cbe, SAADP_form_cbe=SAADP_form_cbe, b12rn_form_cbe=b12rn_form_cbe, b34rn_form_cbe=b34rn_form_cbe, \
		b13srp_form_cbe=b13srp_form_cbe, b4srp_form_cbe=b4srp_form_cbe, asi_form_cbe=asi_form_cbe, \
		TA_form_mev=TA_form_mev, PJ_form_mev=PJ_form_mev, \
		ML_form_mev=ML_form_mev, LSST_form_mev=LSST_form_mev, SDST_form_mev=SDST_form_mev, \
		TDT_form_mev=TDT_form_mev, SAADP_form_mev=SAADP_form_mev, b12rn_form_mev=b12rn_form_mev, \
		b34rn_form_mev=b34rn_form_mev, b13srp_form_mev=b13srp_form_mev, b4srp_form_mev=b4srp_form_mev, asi_form_mev=asi_form_mev)

@app.route('/v12')
def v12_link():
	version = 'v12'
	version_cap = version + '_baseline_cap'
	version_req = version + '_baseline_req'        
	calc = sens_calc(version_cap=version_cap, version_req=version_req)
	inst_cap, inst_req = calc.draw()

	TA_form_cbe = inst_cap['Telescope Aperture (cm)'][0]
	PJ_form_cbe = inst_cap['Pointing Jitter (arcsec)'][0]
	ML_form_cbe = inst_cap['Mission Lifetime (years)'][0]
	LSST_form_cbe = inst_cap['Large Step Slew Time (s)'][0]
	SDST_form_cbe = inst_cap['Small Dither Slew Time (s)'][0]
	TDT_form_cbe = inst_cap['Telemetry Downlink Time (s/orbit)'][0]
	SAADP_form_cbe = inst_cap['South Atlantic Anomaly Down Period (s/orbit)'][0]
	b12rn_form_cbe = inst_cap['Bands']['dQ'][0][0]
	b34rn_form_cbe = inst_cap['Bands']['dQ'][0][2]
	b13srp_form_cbe = inst_cap['Bands']['R'][0][0]
	b4srp_form_cbe = inst_cap['Bands']['R'][0][3]
	asi_form_cbe = inst_cap['Bands']['T_samp'][0][0]

	TA_form_mev = inst_req['Telescope Aperture (cm)'][0]
	PJ_form_mev = inst_req['Pointing Jitter (arcsec)'][0]
	ML_form_mev = inst_req['Mission Lifetime (years)'][0]
	LSST_form_mev = inst_req['Large Step Slew Time (s)'][0]
	SDST_form_mev = inst_req['Small Dither Slew Time (s)'][0]
	TDT_form_mev = inst_req['Telemetry Downlink Time (s/orbit)'][0]
	SAADP_form_mev = inst_req['South Atlantic Anomaly Down Period (s/orbit)'][0]
	b12rn_form_mev = inst_req['Bands']['dQ'][0][0]
	b34rn_form_mev = inst_req['Bands']['dQ'][0][2]
	b13srp_form_mev = inst_req['Bands']['R'][0][0]
	b4srp_form_mev = inst_req['Bands']['R'][0][3]
	asi_form_mev = inst_req['Bands']['T_samp'][0][0]

	version_dict['version_cap'] = version_cap
	version_dict['version_req'] = version_req
	
	return render_template("table_advanced.html", TA_form_cbe=TA_form_cbe, PJ_form_cbe=PJ_form_cbe, \
		ML_form_cbe=ML_form_cbe, \
		LSST_form_cbe=LSST_form_cbe, SDST_form_cbe=SDST_form_cbe, \
		TDT_form_cbe=TDT_form_cbe, SAADP_form_cbe=SAADP_form_cbe, b12rn_form_cbe=b12rn_form_cbe, b34rn_form_cbe=b34rn_form_cbe, \
		b13srp_form_cbe=b13srp_form_cbe, b4srp_form_cbe=b4srp_form_cbe, asi_form_cbe=asi_form_cbe, \
		TA_form_mev=TA_form_mev, PJ_form_mev=PJ_form_mev, \
		ML_form_mev=ML_form_mev, LSST_form_mev=LSST_form_mev, SDST_form_mev=SDST_form_mev, \
		TDT_form_mev=TDT_form_mev, SAADP_form_mev=SAADP_form_mev, b12rn_form_mev=b12rn_form_mev, \
		b34rn_form_mev=b34rn_form_mev, b13srp_form_mev=b13srp_form_mev, b4srp_form_mev=b4srp_form_mev, asi_form_mev=asi_form_mev)

@app.route('/v12_thres')
def v12_th_link():
	version = 'v12_thres'
	version_cap = version + '_cap2'
	version_req = version + '_req2'        
	calc = sens_calc(version_cap=version_cap, version_req=version_req)
	inst_cap, inst_req = calc.draw()

	TA_form_cbe = inst_cap['Telescope Aperture (cm)'][0]
	PJ_form_cbe = inst_cap['Pointing Jitter (arcsec)'][0]
	ML_form_cbe = inst_cap['Mission Lifetime (years)'][0]
	LSST_form_cbe = inst_cap['Large Step Slew Time (s)'][0]
	SDST_form_cbe = inst_cap['Small Dither Slew Time (s)'][0]
	TDT_form_cbe = inst_cap['Telemetry Downlink Time (s/orbit)'][0]
	SAADP_form_cbe = inst_cap['South Atlantic Anomaly Down Period (s/orbit)'][0]
	b12rn_form_cbe = inst_cap['Bands']['dQ'][0][0]
	b34rn_form_cbe = inst_cap['Bands']['dQ'][0][2]
	b13srp_form_cbe = inst_cap['Bands']['R'][0][0]
	b4srp_form_cbe = inst_cap['Bands']['R'][0][3]
	asi_form_cbe = inst_cap['Bands']['T_samp'][0][0]

	TA_form_mev = inst_req['Telescope Aperture (cm)'][0]
	PJ_form_mev = inst_req['Pointing Jitter (arcsec)'][0]
	ML_form_mev = inst_req['Mission Lifetime (years)'][0]
	LSST_form_mev = inst_req['Large Step Slew Time (s)'][0]
	SDST_form_mev = inst_req['Small Dither Slew Time (s)'][0]
	TDT_form_mev = inst_req['Telemetry Downlink Time (s/orbit)'][0]
	SAADP_form_mev = inst_req['South Atlantic Anomaly Down Period (s/orbit)'][0]
	b12rn_form_mev = inst_req['Bands']['dQ'][0][0]
	b34rn_form_mev = inst_req['Bands']['dQ'][0][2]
	b13srp_form_mev = inst_req['Bands']['R'][0][0]
	b4srp_form_mev = inst_req['Bands']['R'][0][3]
	asi_form_mev = inst_req['Bands']['T_samp'][0][0]

	version_dict['version_cap'] = version_cap
	version_dict['version_req'] = version_req
	
	return render_template("table_advanced.html", TA_form_cbe=TA_form_cbe, PJ_form_cbe=PJ_form_cbe, \
		ML_form_cbe=ML_form_cbe, \
		LSST_form_cbe=LSST_form_cbe, SDST_form_cbe=SDST_form_cbe, \
		TDT_form_cbe=TDT_form_cbe, SAADP_form_cbe=SAADP_form_cbe, b12rn_form_cbe=b12rn_form_cbe, b34rn_form_cbe=b34rn_form_cbe, \
		b13srp_form_cbe=b13srp_form_cbe, b4srp_form_cbe=b4srp_form_cbe, asi_form_cbe=asi_form_cbe, \
		TA_form_mev=TA_form_mev, PJ_form_mev=PJ_form_mev, \
		ML_form_mev=ML_form_mev, LSST_form_mev=LSST_form_mev, SDST_form_mev=SDST_form_mev, \
		TDT_form_mev=TDT_form_mev, SAADP_form_mev=SAADP_form_mev, b12rn_form_mev=b12rn_form_mev, \
		b34rn_form_mev=b34rn_form_mev, b13srp_form_mev=b13srp_form_mev, b4srp_form_mev=b4srp_form_mev, asi_form_mev=asi_form_mev)

@app.route('/v13')
def v13_link():
	version = 'v13'
	version_cap = version + '_baseline_cbe'
	version_req = version + '_baseline_mev'        
	calc = sens_calc(version_cap=version_cap, version_req=version_req)
	inst_cap, inst_req = calc.draw()

	TA_form_cbe = inst_cap['Telescope Aperture (cm)'][0]
	PJ_form_cbe = inst_cap['Pointing Jitter (arcsec)'][0]
	ML_form_cbe = inst_cap['Mission Lifetime (years)'][0]
	LSST_form_cbe = inst_cap['Large Step Slew Time (s)'][0]
	SDST_form_cbe = inst_cap['Small Dither Slew Time (s)'][0]
	TDT_form_cbe = inst_cap['Telemetry Downlink Time (s/orbit)'][0]
	SAADP_form_cbe = inst_cap['South Atlantic Anomaly Down Period (s/orbit)'][0]
	b12rn_form_cbe = inst_cap['Bands']['dQ'][0][0]
	b34rn_form_cbe = inst_cap['Bands']['dQ'][0][2]
	b13srp_form_cbe = inst_cap['Bands']['R'][0][0]
	b4srp_form_cbe = inst_cap['Bands']['R'][0][3]
	asi_form_cbe = inst_cap['Bands']['T_samp'][0][0]

	TA_form_mev = inst_req['Telescope Aperture (cm)'][0]
	PJ_form_mev = inst_req['Pointing Jitter (arcsec)'][0]
	ML_form_mev = inst_req['Mission Lifetime (years)'][0]
	LSST_form_mev = inst_req['Large Step Slew Time (s)'][0]
	SDST_form_mev = inst_req['Small Dither Slew Time (s)'][0]
	TDT_form_mev = inst_req['Telemetry Downlink Time (s/orbit)'][0]
	SAADP_form_mev = inst_req['South Atlantic Anomaly Down Period (s/orbit)'][0]
	b12rn_form_mev = inst_req['Bands']['dQ'][0][0]
	b34rn_form_mev = inst_req['Bands']['dQ'][0][2]
	b13srp_form_mev = inst_req['Bands']['R'][0][0]
	b4srp_form_mev = inst_req['Bands']['R'][0][3]
	asi_form_mev = inst_req['Bands']['T_samp'][0][0]

	version_dict['version_cap'] = version_cap
	version_dict['version_req'] = version_req
	
	return render_template("table_advanced.html", TA_form_cbe=TA_form_cbe, PJ_form_cbe=PJ_form_cbe, \
		ML_form_cbe=ML_form_cbe, \
		LSST_form_cbe=LSST_form_cbe, SDST_form_cbe=SDST_form_cbe, \
		TDT_form_cbe=TDT_form_cbe, SAADP_form_cbe=SAADP_form_cbe, b12rn_form_cbe=b12rn_form_cbe, b34rn_form_cbe=b34rn_form_cbe, \
		b13srp_form_cbe=b13srp_form_cbe, b4srp_form_cbe=b4srp_form_cbe, asi_form_cbe=asi_form_cbe, \
		TA_form_mev=TA_form_mev, PJ_form_mev=PJ_form_mev, \
		ML_form_mev=ML_form_mev, LSST_form_mev=LSST_form_mev, SDST_form_mev=SDST_form_mev, \
		TDT_form_mev=TDT_form_mev, SAADP_form_mev=SAADP_form_mev, b12rn_form_mev=b12rn_form_mev, \
		b34rn_form_mev=b34rn_form_mev, b13srp_form_mev=b13srp_form_mev, b4srp_form_mev=b4srp_form_mev, asi_form_mev=asi_form_mev)

@app.route('/v14')
def v14_link():
	version = 'v14'
	version_cap = version + '_baseline_cbe'
	version_req = version + '_baseline_mev'        
	calc = sens_calc(version_cap=version_cap, version_req=version_req)
	inst_cap, inst_req = calc.draw()

	TA_form_cbe = inst_cap['Telescope Aperture (cm)'][0]
	PJ_form_cbe = inst_cap['Pointing Jitter (arcsec)'][0]
	ML_form_cbe = inst_cap['Mission Lifetime (years)'][0]
	LSST_form_cbe = inst_cap['Large Step Slew Time (s)'][0]
	SDST_form_cbe = inst_cap['Small Dither Slew Time (s)'][0]
	TDT_form_cbe = inst_cap['Telemetry Downlink Time (s/orbit)'][0]
	SAADP_form_cbe = inst_cap['South Atlantic Anomaly Down Period (s/orbit)'][0]
	b12rn_form_cbe = inst_cap['Bands']['dQ'][0][0]
	b34rn_form_cbe = inst_cap['Bands']['dQ'][0][2]
	b13srp_form_cbe = inst_cap['Bands']['R'][0][0]
	b4srp_form_cbe = inst_cap['Bands']['R'][0][3]
	asi_form_cbe = inst_cap['Bands']['T_samp'][0][0]

	TA_form_mev = inst_req['Telescope Aperture (cm)'][0]
	PJ_form_mev = inst_req['Pointing Jitter (arcsec)'][0]
	ML_form_mev = inst_req['Mission Lifetime (years)'][0]
	LSST_form_mev = inst_req['Large Step Slew Time (s)'][0]
	SDST_form_mev = inst_req['Small Dither Slew Time (s)'][0]
	TDT_form_mev = inst_req['Telemetry Downlink Time (s/orbit)'][0]
	SAADP_form_mev = inst_req['South Atlantic Anomaly Down Period (s/orbit)'][0]
	b12rn_form_mev = inst_req['Bands']['dQ'][0][0]
	b34rn_form_mev = inst_req['Bands']['dQ'][0][2]
	b13srp_form_mev = inst_req['Bands']['R'][0][0]
	b4srp_form_mev = inst_req['Bands']['R'][0][3]
	asi_form_mev = inst_req['Bands']['T_samp'][0][0]

	version_dict['version_cap'] = version_cap
	version_dict['version_req'] = version_req
	
	return render_template("table_advanced.html", TA_form_cbe=TA_form_cbe, PJ_form_cbe=PJ_form_cbe, \
		ML_form_cbe=ML_form_cbe, \
		LSST_form_cbe=LSST_form_cbe, SDST_form_cbe=SDST_form_cbe, \
		TDT_form_cbe=TDT_form_cbe, SAADP_form_cbe=SAADP_form_cbe, b12rn_form_cbe=b12rn_form_cbe, b34rn_form_cbe=b34rn_form_cbe, \
		b13srp_form_cbe=b13srp_form_cbe, b4srp_form_cbe=b4srp_form_cbe, asi_form_cbe=asi_form_cbe, \
		TA_form_mev=TA_form_mev, PJ_form_mev=PJ_form_mev, \
		ML_form_mev=ML_form_mev, LSST_form_mev=LSST_form_mev, SDST_form_mev=SDST_form_mev, \
		TDT_form_mev=TDT_form_mev, SAADP_form_mev=SAADP_form_mev, b12rn_form_mev=b12rn_form_mev, \
		b34rn_form_mev=b34rn_form_mev, b13srp_form_mev=b13srp_form_mev, b4srp_form_mev=b4srp_form_mev, asi_form_mev=asi_form_mev)

@app.route('/v16')
def v16_link():
	#refresh = execute_js('refresh.js')
	version = 'v16'
	version_cap = version + '_baseline_cbe'
	version_req = version + '_baseline_mev'        
	calc = sens_calc(version_cap=version_cap, version_req=version_req)
	inst_cap, inst_req, sens_cap, sens_req, ZL_fac_cap, ZL_fac_req = calc.draw()

	TA_form_cbe = inst_cap['Telescope Aperture (cm)'][0]
	PJ_form_cbe = inst_cap['Pointing Jitter (arcsec)'][0]
	ML_form_cbe = inst_cap['Mission Lifetime (years)'][0]
	LSST_form_cbe = inst_cap['Large Step Slew Time (s)'][0]
	SDST_form_cbe = inst_cap['Small Dither Slew Time (s)'][0]
	TDT_form_cbe = inst_cap['Telemetry Downlink Time (s/orbit)'][0]
	SAADP_form_cbe = inst_cap['South Atlantic Anomaly Down Period (s/orbit)'][0]
	b12rn_form_cbe = inst_cap['Bands']['dQ'][0][0]
	b34rn_form_cbe = inst_cap['Bands']['dQ'][0][2]
	b13srp_form_cbe = inst_cap['Bands']['R'][0][0]
	b4srp_form_cbe = inst_cap['Bands']['R'][0][3]
	asi_form_cbe = inst_cap['Bands']['T_samp'][0][0]
	TOE_form_cbe = sens_cap['der_char']['eta_tot'][0][0]
	ps_form_cbe = sens_cap['der_char']['th_pix'][0][0]
	zi_form_cbe = ZL_fac_cap
	Asfet_form_cbe = sens_cap['der_char']['t_int_sh'][0]
	Dfet_form_cbe = sens_cap['der_char']['t_int_dp'][0]
	Enopfop_form_cbe = sens_cap['der_char']['Neff'][0][0]
	csf_form_cbe = inst_cap['Channel sampling'][0]
	dfa_form_cbe = inst_cap['Deep field area (sq degrees)'][0]
	noa_form_cbe = inst_cap['nbands']


	TA_form_mev = inst_req['Telescope Aperture (cm)'][0]
	PJ_form_mev = inst_req['Pointing Jitter (arcsec)'][0]
	ML_form_mev = inst_req['Mission Lifetime (years)'][0]
	LSST_form_mev = inst_req['Large Step Slew Time (s)'][0]
	SDST_form_mev = inst_req['Small Dither Slew Time (s)'][0]
	TDT_form_mev = inst_req['Telemetry Downlink Time (s/orbit)'][0]
	SAADP_form_mev = inst_req['South Atlantic Anomaly Down Period (s/orbit)'][0]
	b12rn_form_mev = inst_req['Bands']['dQ'][0][0]
	b34rn_form_mev = inst_req['Bands']['dQ'][0][2]
	b13srp_form_mev = inst_req['Bands']['R'][0][0]
	b4srp_form_mev = inst_req['Bands']['R'][0][3]
	asi_form_mev = inst_req['Bands']['T_samp'][0][0]
	TOE_form_mev = sens_req['der_char']['eta_tot'][0][0]
	ps_form_mev = sens_req['der_char']['th_pix'][0][0]
	zi_form_mev = ZL_fac_req
	Asfet_form_mev = sens_req['der_char']['t_int_sh'][0]
	Dfet_form_mev = sens_req['der_char']['t_int_dp'][0]
	Enopfop_form_mev = sens_req['der_char']['Neff'][0][0]
	csf_form_mev = inst_req['Channel sampling'][0]
	dfa_form_mev = inst_req['Deep field area (sq degrees)'][0]
	noa_form_mev = inst_req['nbands']


	version_dict['version_cap'] = version_cap
	version_dict['version_req'] = version_req
	
	return render_template("table_advanced.html", TA_form_cbe=TA_form_cbe, PJ_form_cbe=PJ_form_cbe, \
		ML_form_cbe=ML_form_cbe, \
		LSST_form_cbe=LSST_form_cbe, SDST_form_cbe=SDST_form_cbe, \
		TDT_form_cbe=TDT_form_cbe, SAADP_form_cbe=SAADP_form_cbe, b12rn_form_cbe=b12rn_form_cbe, b34rn_form_cbe=b34rn_form_cbe, \
		b13srp_form_cbe=b13srp_form_cbe, b4srp_form_cbe=b4srp_form_cbe, asi_form_cbe=asi_form_cbe, TOE_form_cbe=TOE_form_cbe, \
		ps_form_cbe=ps_form_cbe, zi_form_cbe=zi_form_cbe, Asfet_form_cbe=Asfet_form_cbe, Dfet_form_cbe=Dfet_form_cbe, \
		Enopfop_form_cbe=Enopfop_form_cbe, csf_form_cbe=csf_form_cbe, dfa_form_cbe=dfa_form_cbe, noa_form_cbe=noa_form_cbe, \
		TA_form_mev=TA_form_mev, PJ_form_mev=PJ_form_mev, ML_form_mev=ML_form_mev, LSST_form_mev=LSST_form_mev, SDST_form_mev=SDST_form_mev, \
		TDT_form_mev=TDT_form_mev, SAADP_form_mev=SAADP_form_mev, b12rn_form_mev=b12rn_form_mev, \
		b34rn_form_mev=b34rn_form_mev, b13srp_form_mev=b13srp_form_mev, b4srp_form_mev=b4srp_form_mev, asi_form_mev=asi_form_mev, \
		TOE_form_mev=TOE_form_mev, ps_form_mev=ps_form_mev, zi_form_mev=zi_form_mev, Asfet_form_mev=Asfet_form_mev, \
		Dfet_form_mev=Dfet_form_mev, Enopfop_form_mev=Enopfop_form_mev, csf_form_mev=csf_form_mev, dfa_form_mev=dfa_form_mev, \
		noa_form_mev=noa_form_mev)


@app.route('/advanced_parameters', methods=['POST'])
def addRegion_advanced():

	if version_dict['version_cap'] == 'v16_baseline_cbe':
		IV_CBE = {'Bands':Bands_cbe_16}
		IV_MEV = {'Bands':Bands_mev_16}
	elif version_dict['version_cap'] == 'v14_baseline_cbe':
		IV_CBE = {'Bands':Bands_cbe_14}
		IV_MEV = {'Bands':Bands_mev_14}
	elif version_dict['version_cap'] == 'v13_baseline_cbe':
		IV_CBE = {'Bands':Bands_cbe_13}
		IV_MEV = {'Bands':Bands_mev_13}
	elif version_dict['version_cap'] == 'v12_thres_cap2':
		IV_CBE = {'Bands':Bands_cbe_12_thres}
		IV_MEV = {'Bands':Bands_mev_12_thres}
	elif version_dict['version_cap'] == 'v12_baseline_cap':
		IV_CBE = {'Bands':Bands_cbe_12}
		IV_MEV = {'Bands':Bands_mev_12}
	elif version_dict['version_cap'] == 'v8_thresv2_cap':
		IV_CBE = {'Bands':Bands_cbe_thresv2_8}
		IV_MEV = {'Bands':Bands_mev_thresv2_8}
	elif version_dict['version_cap'] == 'v8_thresv1_cap':
		IV_CBE = {'Bands':Bands_cbe_thresv1_8}
		IV_MEV = {'Bands':Bands_mev_thresv1_8}
	elif version_dict['version_cap'] == 'v8_baseline_cap':
		IV_CBE = {'Bands':Bands_cbe_8}
		IV_MEV = {'Bands':Bands_mev_8}
	elif version_dict['version_cap'] == 'v7_capability':
		IV_CBE = {'Bands':Bands_cbe_7}
		IV_MEV = {'Bands':Bands_mev_7}
	else:
		pass

	IV_CBE['Telescope Aperture (cm)'] = (float(request.form['Telescope Aperture cbe(cm)']), 'cm')
	IV_CBE['Pointing Jitter (arcsec)'] = (float(request.form['Pointing Jitter cbe(arcsec)']), 'arcsec')
	IV_CBE['Mission Lifetime (years)'] = (float(request.form['Mission Lifetime cbe(years)']), 'yr')
	IV_CBE['Large Step Slew Time (s)'] = (float(request.form['Large Step Slew Time cbe(s)']), 's')
	IV_CBE['Small Dither Slew Time (s)'] = (float(request.form['Small Dither Slew Time cbe(s)']), 's')
	IV_CBE['Telemetry Downlink Time (s/orbit)'] = (float(request.form['Telemetry Downlink Time cbe(s/orbit)']), 'p.orb.')
	IV_CBE['South Atlantic Anomaly Down Period (s/orbit)'] = (float(request.form['South Atlantic Anomaly Down Period cbe(s/orbit)']), 'p.orb.')
	IV_CBE['Bands']['dQ'][0][0:2] = (float(request.form['band 1-2 read noise cbe(e-)']))
	#IV_CBE['Bands']['dQ'][0][1] = IV_CBE['Bands']['dQ'][0][0]
	IV_CBE['Bands']['dQ'][0][2:4] = (float(request.form['band 3-4 read noise cbe(e-)']))
	#IV_CBE['Bands']['dQ'][0][3] = IV_CBE['Bands']['dQ'][0][2]
	IV_CBE['Bands']['R'][0][0:3] = (float(request.form['band 1-3 spectral resolving power cbe']))
	#IV_CBE['Bands']['R'][0][1] = IV_CBE['Bands']['R'][0][0]
	#IV_CBE['Bands']['R'][0][2] = IV_CBE['Bands']['R'][0][0]
	IV_CBE['Bands']['R'][0][3] = (float(request.form['band 4 spectral resolving power cbe']))
	IV_CBE['Bands']['T_samp'][0][:] = (float(request.form['array sampling interval cbe(s)']))
	DERIVED_CBE['eta_tot'] = (float(request.form['Total Optical Efficiency cbe']))
	DERIVED_CBE['th_pix'] = (float(request.form['pixel size cbe(arcsec)']))
	DERIVED_CBE['ZL_fac'] = (float(request.form['zodi intensity at 2 um cbe(ZL_factor)']))
	DERIVED_CBE['Asfet'] = (float(request.form['All-sky field exposure time cbe(s)']))
	DERIVED_CBE['Dfet'] = (float(request.form['Deep field exposure time cbe(s)']))
	DERIVED_CBE['Neff'] = (float(request.form['Effective number of pixels for optimal photometry cbe(s)']))
	IV_CBE['Channel sampling'] = (float(request.form['channel sampling factor cbe(Nyq/2)']), 'Nyq/2')
	IV_CBE['Deep field area (sq degrees)'] = (float(request.form['deep field area cbe(sq deg)']), 'Nyq/2')
	IV_CBE['nbands'] = (int(request.form['number of arrays cbe']))



	IV_MEV['Telescope Aperture (cm)'] = (float(request.form['Telescope Aperture mev(cm)']), 'cm')
	IV_MEV['Pointing Jitter (arcsec)'] = (float(request.form['Pointing Jitter mev(arcsec)']), 'arcsec')
	IV_MEV['Mission Lifetime (years)'] = (float(request.form['Mission Lifetime mev(years)']), 'yr')
	IV_MEV['Large Step Slew Time (s)'] = (float(request.form['Large Step Slew Time mev(s)']), 's')
	IV_MEV['Small Dither Slew Time (s)'] = (float(request.form['Small Dither Slew Time mev(s)']), 's')
	IV_MEV['Telemetry Downlink Time (s/orbit)'] = (float(request.form['Telemetry Downlink Time mev(s/orbit)']), 'p.orb.')
	IV_MEV['South Atlantic Anomaly Down Period (s/orbit)'] = (float(request.form['South Atlantic Anomaly Down Period mev(s/orbit)']), 'p.orb.')
	IV_MEV['Bands']['dQ'][0][0:1] = (float(request.form['band 1-2 read noise mev(e-)']))
	#IV_MEV['Bands']['dQ'][0][1] = IV_MEV['Bands']['dQ'][0][0]
	IV_MEV['Bands']['dQ'][0][2:3] = (float(request.form['band 3-4 read noise mev(e-)']))
	#IV_MEV['Bands']['dQ'][0][3] = IV_MEV['Bands']['dQ'][0][2]
	IV_MEV['Bands']['R'][0][0:2] = (float(request.form['band 1-3 spectral resolving power mev']))
	#IV_MEV['Bands']['R'][0][1] = IV_MEV['Bands']['R'][0][0]
	#IV_MEV['Bands']['R'][0][2] = IV_MEV['Bands']['R'][0][0]
	IV_MEV['Bands']['R'][0][3] = (float(request.form['band 4 spectral resolving power mev']))
	IV_MEV['Bands']['T_samp'][0][:] = (float(request.form['array sampling interval mev(s)']))
	DERIVED_MEV['eta_tot'] = (float(request.form['Total Optical Efficiency mev']))
	DERIVED_MEV['th_pix'] = (float(request.form['pixel size mev(arcsec)']))
	DERIVED_MEV['ZL_fac'] = (float(request.form['zodi intensity at 2 um mev(ZL_factor)']))
	DERIVED_MEV['Asfet'] = (float(request.form['All-sky field exposure time mev(s)']))
	DERIVED_MEV['Dfet'] = (float(request.form['Deep field exposure time mev(s)']))
	DERIVED_MEV['Neff'] = (float(request.form['Effective number of pixels for optimal photometry mev(s)']))
	IV_MEV['Channel sampling'] = (float(request.form['channel sampling factor mev(Nyq/2)']), 'Nyq/2')
	IV_MEV['Deep field area (sq degrees)'] = (float(request.form['deep field area mev(sq deg)']), 'Nyq/2')
	IV_MEV['nbands'] = (int(request.form['number of arrays mev']))


	calc = sens_calc(version_cap=version_dict['version_cap'], version_req=version_dict['version_req'])
	inst_cap, inst_req, sens_cap, sens_req, ZL_fac_cap, ZL_fac_req = calc.draw(inst_cap_entry=IV_CBE, inst_req_entry=IV_MEV, DERIVED_CBE=DERIVED_CBE, DERIVED_MEV=DERIVED_MEV)
	TA_form_cbe = inst_cap['Telescope Aperture (cm)'][0]
	PJ_form_cbe = inst_cap['Pointing Jitter (arcsec)'][0]
	ML_form_cbe = inst_cap['Mission Lifetime (years)'][0]
	LSST_form_cbe = inst_cap['Large Step Slew Time (s)'][0]
	SDST_form_cbe = inst_cap['Small Dither Slew Time (s)'][0]
	TDT_form_cbe = inst_cap['Telemetry Downlink Time (s/orbit)'][0]
	SAADP_form_cbe = inst_cap['South Atlantic Anomaly Down Period (s/orbit)'][0]
	b12rn_form_cbe = inst_cap['Bands']['dQ'][0][0]
	b34rn_form_cbe = inst_cap['Bands']['dQ'][0][2]
	b13srp_form_cbe = inst_cap['Bands']['R'][0][0]
	b4srp_form_cbe = inst_cap['Bands']['R'][0][3]
	asi_form_cbe = inst_cap['Bands']['T_samp'][0][0]
	TOE_form_cbe = sens_cap['der_char']['eta_tot'][0][0]
	ps_form_cbe = sens_cap['der_char']['th_pix'][0][0]
	zi_form_cbe = ZL_fac_cap
	Asfet_form_cbe = sens_cap['der_char']['t_int_sh'][0]
	Dfet_form_cbe = sens_cap['der_char']['t_int_dp'][0]
	Enopfop_form_cbe = sens_cap['der_char']['Neff'][0][0]
	csf_form_cbe = inst_cap['Channel sampling'][0]
	dfa_form_cbe = inst_cap['Deep field area (sq degrees)'][0]
	noa_form_cbe = inst_cap['nbands']


	TA_form_mev = inst_req['Telescope Aperture (cm)'][0]
	PJ_form_mev = inst_req['Pointing Jitter (arcsec)'][0]
	ML_form_mev = inst_req['Mission Lifetime (years)'][0]
	LSST_form_mev = inst_req['Large Step Slew Time (s)'][0]
	SDST_form_mev = inst_req['Small Dither Slew Time (s)'][0]
	TDT_form_mev = inst_req['Telemetry Downlink Time (s/orbit)'][0]
	SAADP_form_mev = inst_req['South Atlantic Anomaly Down Period (s/orbit)'][0]
	b12rn_form_mev = inst_req['Bands']['dQ'][0][0]
	b34rn_form_mev = inst_req['Bands']['dQ'][0][2]
	b13srp_form_mev = inst_req['Bands']['R'][0][0]
	b4srp_form_mev = inst_req['Bands']['R'][0][3]
	asi_form_mev = inst_req['Bands']['T_samp'][0][0]
	TOE_form_mev = sens_req['der_char']['eta_tot'][0][0]
	ps_form_mev = sens_req['der_char']['th_pix'][0][0]
	zi_form_mev = ZL_fac_req
	Asfet_form_mev = sens_req['der_char']['t_int_sh'][0]
	Dfet_form_mev = sens_req['der_char']['t_int_dp'][0]
	Enopfop_form_mev = sens_req['der_char']['Neff'][0][0]
	csf_form_mev = inst_req['Channel sampling'][0]
	dfa_form_mev = inst_req['Deep field area (sq degrees)'][0]
	noa_form_mev = inst_req['nbands']



	return render_template("table_advanced.html", TA_form_cbe=TA_form_cbe, PJ_form_cbe=PJ_form_cbe, \
		ML_form_cbe=ML_form_cbe, \
		LSST_form_cbe=LSST_form_cbe, SDST_form_cbe=SDST_form_cbe, \
		TDT_form_cbe=TDT_form_cbe, SAADP_form_cbe=SAADP_form_cbe, b12rn_form_cbe=b12rn_form_cbe, b34rn_form_cbe=b34rn_form_cbe, \
		b13srp_form_cbe=b13srp_form_cbe, b4srp_form_cbe=b4srp_form_cbe, asi_form_cbe=asi_form_cbe, TOE_form_cbe=TOE_form_cbe, \
		ps_form_cbe=ps_form_cbe, zi_form_cbe=zi_form_cbe, Asfet_form_cbe=Asfet_form_cbe, Dfet_form_cbe=Dfet_form_cbe, \
		Enopfop_form_cbe=Enopfop_form_cbe, csf_form_cbe=csf_form_cbe, dfa_form_cbe=dfa_form_cbe, noa_form_cbe=noa_form_cbe, \
		TA_form_mev=TA_form_mev, PJ_form_mev=PJ_form_mev, ML_form_mev=ML_form_mev, LSST_form_mev=LSST_form_mev, SDST_form_mev=SDST_form_mev, \
		TDT_form_mev=TDT_form_mev, SAADP_form_mev=SAADP_form_mev, b12rn_form_mev=b12rn_form_mev, \
		b34rn_form_mev=b34rn_form_mev, b13srp_form_mev=b13srp_form_mev, b4srp_form_mev=b4srp_form_mev, asi_form_mev=asi_form_mev, \
		TOE_form_mev=TOE_form_mev, ps_form_mev=ps_form_mev, zi_form_mev=zi_form_mev, Asfet_form_mev=Asfet_form_mev, \
		Dfet_form_mev=Dfet_form_mev, Enopfop_form_mev=Enopfop_form_mev, csf_form_mev=csf_form_mev, dfa_form_mev=dfa_form_mev, \
		noa_form_mev=noa_form_mev)


@app.route('/plot1')
def plot1():
	#img = v7()
	try:
		path = '/Users/yolo_mac/web_gui_v2/static/'
		return send_file(path + 'image1.png')
		#return get_send_file_max_age(path + 'image1.png')
	except IOError:
		pass

@app.route('/plot2')
def plot2():
	try:
		path = '/Users/yolo_mac/web_gui_v2/static/'
		return send_file(path + 'image2.png')
	except IOError:
		pass

@app.route('/plot3')
def plot3():
	try:
		path = '/Users/yolo_mac/web_gui_v2/static/'
		return send_file(path + 'image3.png')
	except IOError:
		pass



if __name__=="__main__":
	app.run(debug=True)


