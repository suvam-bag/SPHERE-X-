#!/usr/bin/env python
from numpy import arange,sin,pi,cos,tan
import simap_util as sut
from plot_Mab_lambda_prime_prop import plot_Mab_lambda_prime_prop
from plot_Mab_lambda_prop import plot_Mab_lambda_prop
from plot_sb_lambda_prime_prop import plot_sb_lambda_prime_prop
import matplotlib
from matplotlib import style # To customize matplotlib's plot styles
import numpy as np
import pylab as pl 
import time
import matplotlib.pyplot as plt
import cv2



VERSIONS_GUI = ('','v2','v4','v6','v6_threshold','v7_capability','v7_required','v7_threshold','v8_baseline_cap','v8_baseline_req','v8_thresv1_cap','v8_thresv1_req','v8_thresv2_cap','v8_thresv2_req','v12_baseline_cap','v12_baseline_req','v12_thres_cap2','v12_thres_req2','v13_baseline_mev','v13_baseline_cbe','v14_baseline_mev','v14_baseline_cbe','v16_baseline_mev','v16_baseline_cbe')

VERSIONS = ('','v7','v8','v8_thresv1','v8_thresv2','v12','v12_thresh','v13','v14','v16')

#Color choices 
blue1 ='#082a4c'
blue2 ='#111199'
blue3 ='#701978'
black1= '#4c4c4c'
lighGray='#e5e5e5'


class sens_calc(object):

	
	def __init__(self, version_cap=False, version_req=False):
		self.version_cap = version_cap
		self.version_req = version_req
	
	'''
	def convert(self):		
		path = '/Users/yolo_mac/web_gui/static/'
		self.img = cv2.imread(path + 'pumpkin_PNG9366.png', 0)
		cv2.imwrite(path + 'image1.png', self.img)
		return self.img

	'''

	def draw(self, inst_cap_entry=None, inst_req_entry=None, DERIVED_CBE=None, DERIVED_MEV=None):
		c_val = None
		surveys_def = sut.define_surveys()
		bands_def   = sut.define_astro_bands()
		inst_cap = sut.define_instrument(version=self.version_cap)
		#print inst_cap['Bands']['dQ'][0][0]
		#print inst_cap['Bands']['dQ'][0][1]
		#print inst_cap['Bands']['dQ'][0][2]
		#print inst_cap['Bands']['dQ'][0][3]
		inst_req = sut.define_instrument(version=self.version_req)
		if inst_req_entry != None and inst_cap_entry != None:
			#update the key values in inst_req dictionary from inst_req_entry
			for key1, value1 in inst_req.iteritems():
				#if key1 != 'nbands':
				for key2, value2 in inst_req_entry.iteritems():
					if key1 == key2:
						# if key1 == 'Telescope Aperture (cm)':
						# 	c_val = 20.0
						# elif key1 == 'Pointing Jitter (arcsec)':
						# 	c_val = 3
						# elif key1 == 'f number':
						# 	c_val = 3.0
						# elif key1 == 'Deep field area (sq degrees)':
						# 	c_val = 200.0
						# elif key1 == 'Mission Lifetime (years)':
						# 	c_val = 3.0
						# elif key1 == 'nbands':
						# 	c_val = 4
						# elif key1 == 'Orbital period (s)':
						# 	c_val = 95
						# elif key1 == 'Large Step Slew Time (s)':
						# 	c_val = 150.0
						# elif key1 == 'Small Dither Slew Time (s)':
						# 	c_val = 15.0
						# elif key1 == 'Survey redundancy factor (/year)':
						# 	c_val = 3.0
						# elif key1 == 'Channel sampling':
						# 	c_val = 1.0
						# elif key1 == 'Deep All-Sky Survey Steps (/orbit)':
						# 	c_val = 3.0	
						# elif key1 == 'Large All Sky Steps (/orbit)':
						# 	c_val = 4.0
						# elif key1 == 'All Sky Dither Steps (/large step)':
						# 	c_val = 3.0
						# elif key1 == 'Pixel Wavelength (microns)':
						# 	c_val = 4.0
						# elif key1 == 'Telemetry Downlink Time (s/orbit)':
						# 	c_val = 30.0
						# elif key1 == 'South Atlantic Anomaly Down Period (s/orbit)':
						# 	c_val = 86.0
						# else:
						# 	pass
						# if value2[0] != c_val or value2 != c_val:#so that the values not entered by the user are not considered, hence verison values are retained
						inst_req[key1] = inst_req_entry[key2]

			
			for key3, value3 in inst_cap.iteritems():
				for key4, value4 in inst_cap_entry.iteritems():
					if key3 == key4:
						inst_cap[key3] = inst_cap_entry[key4]

			sens_cap, ZL_fac_cap = sut.compute_sensitivities(Inst=inst_cap,verbose=False,DERIVED=DERIVED_CBE)
			sens_req, ZL_fac_req = sut.compute_sensitivities(Inst=inst_req,verbose=False,DERIVED=DERIVED_MEV)        



			#self.figure1=matplotlib.figure.Figure(figsize=(7,7),dpi=100)
			self.figure1=pl.figure(0)
			self.figure1.subplots_adjust(left=0.13, bottom=0.11, top=0.97, hspace=0.0, wspace=0.0,right=0.96)
			self.a1=self.figure1.add_subplot(111)
			plot_Mab_lambda_prime_prop(self.a1, surveys_def, bands_def, sens_cap, sens_req)



			#self.figure2=matplotlib.figure.Figure(figsize=(7,7),dpi=100)
			self.figure2=pl.figure(0)
			self.figure2.subplots_adjust(left=0.13, bottom=0.11, top=0.97, hspace=0.0, wspace=0.0,right=0.96)
			self.a2=self.figure2.add_subplot(111)
			plot_Mab_lambda_prop(self.a2, surveys_def, bands_def, sens_cap, sens_req)



			#self.figure3=matplotlib.figure.Figure(figsize=(7,7),dpi=100)
			self.figure3=pl.figure(0)
			#self.figure3.subplots_adjust(left=0.13, bottom=0.11, top=0.97, hspace=0.0, wspace=0.0,right=0.96)
			self.figure3.subplots_adjust(left=0.13, bottom=0.11, top=0.97, hspace=0.0, wspace=0.0,right=0.96)
			self.a3=self.figure3.add_subplot(111)   
			plot_sb_lambda_prime_prop(self.a3, surveys_def, bands_def, sens_cap, sens_req)

			return inst_cap, inst_req, sens_cap, sens_req, ZL_fac_cap, ZL_fac_req
								
		else:
	
			sens_cap, ZL_fac_cap = sut.compute_sensitivities(Inst=inst_cap,verbose=False,DERIVED=DERIVED_CBE)
			sens_req, ZL_fac_req = sut.compute_sensitivities(Inst=inst_req,verbose=False,DERIVED=DERIVED_MEV)        



			#self.figure1=matplotlib.figure.Figure(figsize=(7,7),dpi=100)
			self.figure1=pl.figure(0)
			self.figure1.subplots_adjust(left=0.13, bottom=0.11, top=0.97, hspace=0.0, wspace=0.0,right=0.96)
			self.a1=self.figure1.add_subplot(111)
			plot_Mab_lambda_prime_prop(self.a1, surveys_def, bands_def, sens_cap, sens_req)



			#self.figure2=matplotlib.figure.Figure(figsize=(7,7),dpi=100)
			self.figure2=pl.figure(0)
			self.figure2.subplots_adjust(left=0.13, bottom=0.11, top=0.97, hspace=0.0, wspace=0.0,right=0.96)
			self.a2=self.figure2.add_subplot(111)
			plot_Mab_lambda_prop(self.a2, surveys_def, bands_def, sens_cap, sens_req)



			#self.figure3=matplotlib.figure.Figure(figsize=(7,7),dpi=100)
			self.figure3=pl.figure(0)
			#self.figure3.subplots_adjust(left=0.13, bottom=0.11, top=0.97, hspace=0.0, wspace=0.0,right=0.96)
			self.figure3.subplots_adjust(left=0.13, bottom=0.11, top=0.97, hspace=0.0, wspace=0.0,right=0.96)
			self.a3=self.figure3.add_subplot(111)   
			plot_sb_lambda_prime_prop(self.a3, surveys_def, bands_def, sens_cap, sens_req)

			return inst_cap, inst_req, sens_cap, sens_req, ZL_fac_cap, ZL_fac_req
		

		

		


		


















