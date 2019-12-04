import numpy as np
import skfuzzy as fuzzy
import matplotlib.pyplot as plt

#Initialize Range
cognitive = np.arange(0,37,1)
cog_level = {}
cog_level["low"] = fuzzy.trapmf(cognitive,[0,0,12,24])
cog_level["med"] = fuzzy.trimf(cognitive,[20,26,33])
cog_level["high"] = fuzzy.trapmf(cognitive,[32,34,36,36])
# c_Low = fuzzy.trapmf(cognitive,[0,0,12,24])
# c_Med = fuzzy.trimf(cognitive,[20,26,33])
# c_High = fuzzy.trapmf(cognitive,[32,34,36,36])

social = np.arange(0,53,1)
soc_level = {}
soc_level["low"] = fuzzy.trapmf(social,[0,0,16,32])
soc_level["med"] = fuzzy.trimf(social,[29,36,44])
soc_level["high"] = fuzzy.trapmf(social,[41,46,52,52])
# s_Low = fuzzy.trapmf(social,[0,0,16,32])
# s_Med = fuzzy.trimf(social,[29,36,44])
# s_High = fuzzy.trapmf(social,[41,46,52,52])

emotional = np.arange(0,53,1)
emo_level = {}
emo_level["low"] = fuzzy.trapmf(emotional,[0,0,18,37])
emo_level["med"] = fuzzy.trimf(emotional,[34,39,44])
emo_level["high"] = fuzzy.trapmf(emotional,[41,46,52,52])
# e_Low = fuzzy.trapmf(emotional,[0,0,18,37])
# e_Med = fuzzy.trimf(emotional,[34,39,44])
# e_High = fuzzy.trapmf(emotional,[41,46,52,52])

spiritual = np.arange(0,45,1)
spi_level = {}
spi_level["low"] = fuzzy.trapmf(spiritual,[0,0,13,26])
spi_level["med"] = fuzzy.trimf(spiritual,[24,31,39])
spi_level["high"] = fuzzy.trapmf(spiritual,[37,40,44,44])
# sp_Low = fuzzy.trapmf(spiritual,[0,0,13,26])
# sp_Med = fuzzy.trimf(spiritual,[24,31,39])
# sp_High = fuzzy.trapmf(spiritual,[37,40,44,44])

physical = np.arange(0,46,1)
phy_level = {}
phy_level["low"] = fuzzy.trapmf(physical,[0,0,12,25])
phy_level["med"] = fuzzy.trimf(physical,[22,29,37])
phy_level["high"] = fuzzy.trapmf(physical,[35,40,45,45])

output = np.arange(0,251,1)
out_level = {}
out_level["vhigh"] = fuzzy.trapmf(output,[0,0,85,110])
out_level["high"] = fuzzy.trimf(output,[90,120,155])
out_level["med"] = fuzzy.trimf(output,[140,155,175])
out_level["low"] = fuzzy.trimf(output,[160,180,200])
out_level["vlow"] = fuzzy.trapmf(output,[180,220,250,250])

fig, (aCog, aSoc, aEmo, aSpi, aPhy) = plt.subplots(nrows=5, figsize=(8, 9))

#Cognitive Plot
aCog.plot(cognitive, cog_level["low"], 'r', linewidth=2, label='Low')
aCog.plot(cognitive, cog_level["med"], 'y', linewidth=2, label='Medium')
aCog.plot(cognitive, cog_level["high"], 'g', linewidth=2, label='High')
aCog.set_title('Cognitive')
aCog.legend()

#Social Plot
aSoc.plot(social, soc_level["low"], 'r', linewidth=2, label='Low')
aSoc.plot(social, soc_level["med"], 'y', linewidth=2, label='Medium')
aSoc.plot(social, soc_level["high"], 'g', linewidth=2, label='High')
aSoc.set_title('Social')
aSoc.legend()

#Emotional Plot
aEmo.plot(emotional, emo_level["low"], 'r', linewidth=2, label='Low')
aEmo.plot(emotional, emo_level["med"], 'y', linewidth=2, label='Medium')
aEmo.plot(emotional, emo_level["high"], 'g', linewidth=2, label='High')
aEmo.set_title('Emotional')
aEmo.legend()

#Spiritual Plot
aSpi.plot(spiritual, spi_level["low"], 'r', linewidth=2, label='Low')
aSpi.plot(spiritual, spi_level["med"], 'y', linewidth=2, label='Medium')
aSpi.plot(spiritual, spi_level["high"], 'g', linewidth=2, label='High')
aSpi.set_title('Spiritual')
aSpi.legend()

#Physical Plot
aPhy.plot(physical, phy_level["low"], 'r', linewidth=2, label='Low')
aPhy.plot(physical, phy_level["med"], 'y', linewidth=2, label='Medium')
aPhy.plot(physical, phy_level["high"], 'g', linewidth=2, label='High')
aPhy.set_title('Physical')
aPhy.legend()


# Turn off top/right axes
for ax in (aCog, aSoc, aEmo, aSpi, aPhy):
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.get_xaxis().tick_bottom()
    ax.get_yaxis().tick_left()

plt.tight_layout()
plt.show()

#Input Graph
input_cog = 20
input_soc = 20
input_emo = 20
input_spi = 20
input_phy = 20

cog = {}
cog["low"] = fuzzy.interp_membership(cognitive, cog_level["low"], input_cog)
cog["med"] = fuzzy.interp_membership(cognitive, cog_level["med"], input_cog)
cog["high"] = fuzzy.interp_membership(cognitive, cog_level["high"], input_cog)

soc = {}
soc["low"] = fuzzy.interp_membership(social, soc_level["low"], input_soc)
soc["med"] = fuzzy.interp_membership(social, soc_level["med"], input_soc)
soc["high"] = fuzzy.interp_membership(social, soc_level["high"], input_soc)

emo = {}
emo["low"] = fuzzy.interp_membership(emotional, emo_level["low"], input_emo)
emo["med"] = fuzzy.interp_membership(emotional, emo_level["med"], input_emo)
emo["high"] = fuzzy.interp_membership(emotional, emo_level["high"], input_emo)

spi = {}
spi["low"] = fuzzy.interp_membership(spiritual, spi_level["low"], input_spi)
spi["med"] = fuzzy.interp_membership(spiritual, spi_level["med"], input_spi)
spi["high"] = fuzzy.interp_membership(spiritual, spi_level["high"], input_spi)

phy = {}
phy["low"] = fuzzy.interp_membership(physical, phy_level["low"], input_phy)
phy["med"] = fuzzy.interp_membership(physical, phy_level["med"], input_phy)
phy["high"] = fuzzy.interp_membership(physical, phy_level["high"], input_phy)

#<----- Create Rules Here ----->
rules_vhigh = {}
rules_vhigh["1"] = np.fmin(cog["low"], np.fmin(soc["low"], np.fmin(emo["low"],np.fmin(spi["low"],phy["low"]))))


rules_high = {}
rules_high["1"] = np.fmin(cog["med"], np.fmin(soc["low"], np.fmin(emo["low"],np.fmin(spi["low"],phy["low"]))))

rules_med = {}
rules_med["1"] = np.fmin(cog["med"], np.fmin(soc["low"], np.fmin(emo["low"],np.fmin(spi["low"],phy["low"]))))

rules_low = {}
rules_low["1"] = np.fmin(cog["med"], np.fmin(soc["high"], np.fmin(emo["low"],np.fmin(spi["low"],phy["high"]))))

rules_vlow = {}
rules_vlow["1"] = np.fmin(cog["high"], np.fmin(soc["high"], np.fmin(emo["high"],np.fmin(spi["high"],phy["high"]))))

# print(rules_vhigh["1"])
# print(rules_high["1"])
# print(rules_med["1"])
# print(rules_low["1"])
# print(rules_vlow["1"])

#<---- Create Output ----->
out = {}
#Compare with
out["vhigh"] = np.fmin(rules_vhigh["1"],out_level["vhigh"])
out["high"] = np.fmin(rules_high["1"],out_level["high"])
out["med"] = np.fmin(rules_med["1"],out_level["med"])
out["low"] = np.fmin(rules_low["1"],out_level["low"])
out["vlow"] = np.fmin(rules_vlow["1"],out_level["vlow"])
# print(f"VHigh = {out['vhigh']} \n")
# #       f"High = {out['high']} \n"
# #       f"Med = {out['med']} \n"
# #       f"Low = {out['low']} \n"
# #       f"Vlow = {out['vlow']} \n")
out0 = np.zeros_like(output)
#<------ Create Defuzzification ---->
aggregated = np.fmax(out["vhigh"],np.fmax(out["high"],np.fmax(out["med"],np.fmax(out["low"],out["vlow"]))))
# aggregated = out["vhigh"]

clean_aggregated = fuzzy.defuzz(output,aggregated, 'centroid')
print(clean_aggregated)
clean_activation = fuzzy.interp_membership(output,aggregated,clean_aggregated)

fig, (cOut, cAgr) = plt.subplots(nrows=2, figsize=(8, 9))

cOut.fill_between(output, out0, out["vhigh"], facecolor='b', alpha=0.7)
cOut.plot(output, out_level["vhigh"], 'r', linewidth=2, linestyle='--', )
cOut.fill_between(output, out0, out["high"], facecolor='g', alpha=0.7)
cOut.plot(output, out_level["high"], 'y', linewidth=2, linestyle='--')
cOut.fill_between(output, out0, out["med"], facecolor='r', alpha=0.7)
cOut.plot(output, out_level["med"], 'g', linewidth=2, linestyle='--')
cOut.fill_between(output, out0, out["low"], facecolor='r', alpha=0.7)
cOut.plot(output, out_level["low"], 'y', linewidth=2, linestyle='--')
cOut.fill_between(output, out0, out["vlow"], facecolor='r', alpha=0.7)
cOut.plot(output, out_level["vlow"], 'g', linewidth=2, linestyle='--')
cOut.set_title('Output')

cAgr.plot(output, out_level["vhigh"], 'r', linewidth=2, linestyle='--', )
cAgr.plot(output, out_level["high"], 'y', linewidth=2, linestyle='--', )
cAgr.plot(output, out_level["med"], 'g', linewidth=2, linestyle='--', )
cAgr.plot(output, out_level["low"], 'y', linewidth=2, linestyle='--', )
cAgr.plot(output, out_level["vlow"], 'g', linewidth=2, linestyle='--', )
cAgr.fill_between(output, out0, aggregated, facecolor='Orange', alpha=0.7)
cAgr.plot([clean_aggregated, clean_aggregated], [0, clean_activation], 'k', linewidth=1.5, alpha=0.9)
cAgr.set_title('Mamdani Output')


# Turn off top/right axes
for ax in (cOut,cAgr):
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.get_xaxis().tick_bottom()
    ax.get_yaxis().tick_left()

plt.tight_layout()
plt.show()
# print(aggregated)
# print(clean_activation)
# print(aggregated)

