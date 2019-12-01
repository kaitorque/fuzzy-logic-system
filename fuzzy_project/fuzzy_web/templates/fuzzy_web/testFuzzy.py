import numpy as np
import skfuzzy as fuzzy
import skfuzzy.control as ctrl
from skfuzzy.control import controlsystem as cts
import matplotlib.pyplot as plt

#Antecedent is used for input parameters and Consequent is used for output. Here ca,mte,ete are input and cgpa is output.
cognitive=ctrl.Antecedent(np.arange(0,37,1),'cognitive') #cognitive marks range 0-36
social=ctrl.Antecedent(np.arange(0,53,1),'social') #social marks range 0-52
emotional=ctrl.Antecedent(np.arange(0,53,1),'emotional') #emotional marks range 0-52
spiritual=ctrl.Antecedent(np.arange(0,45,1),'spiritual') #spiritual marks range 0-44
physical=ctrl.Antecedent(np.arange(0,46,1),'physical') #physical marks range 0-45
output=ctrl.Consequent(np.arange(0,251,1),'output') #output between 0-250
#Cognitive
cognitive['low']=fuzzy.trapmf(cognitive.universe,[0,0,12,24])
cognitive['med']=fuzzy.trimf(cognitive.universe,[20,26.5,33])
cognitive['high']=fuzzy.trapmf(cognitive.universe,[32,34,36,36])
#Social
social['low']=fuzzy.trapmf(social.universe,[0,0,16,32])
social['med']=fuzzy.trimf(social.universe,[29,36.5,44])
social['high']=fuzzy.trapmf(social.universe,[41,46.5,52,52])
#Emotional
emotional['low']=fuzzy.trapmf(emotional.universe,[0,0,18.5,37])
emotional['med']=fuzzy.trimf(emotional.universe,[34,39,44])
emotional['high']=fuzzy.trapmf(emotional.universe,[41,46.5,52,52])
#Spiritual
spiritual['low']=fuzzy.trapmf(spiritual.universe,[0,0,13,26])
spiritual['med']=fuzzy.trimf(spiritual.universe,[24,31.5,39])
spiritual['high']=fuzzy.trapmf(spiritual.universe,[37,40.5,44,44])
#Physical
physical['low']=fuzzy.trapmf(physical.universe,[0,0,12.5,25])
physical['med']=fuzzy.trimf(physical.universe,[22,29.5,37])
physical['high']=fuzzy.trapmf(physical.universe,[35,40,45,45])
#Output
output['vhigh']=fuzzy.trapmf(output.universe,[0,0,85,110])
output['high']=fuzzy.trimf(output.universe,[90,120,155])
output['med']=fuzzy.trimf(output.universe,[140,155,175])
output['low']=fuzzy.trimf(output.universe,[160,180,200])
output['vlow']=fuzzy.trapmf(output.universe,[180,220,250,250])

cognitive.view()
social.view()
emotional.view()
physical.view()
spiritual.view()
output.view()
plt.show()

#now we will decide rules based on creteria of ca, mte and ete.
rule1=ctrl.Rule(cognitive['low'] & social['low'] & emotional['low'] & spiritual['low'] & physical['low'],output['vhigh'])
rule2=ctrl.Rule(cognitive['low'] & social['low'] & emotional['low'] & spiritual['low'] & physical['med'],output['vhigh'])
rule3=ctrl.Rule(cognitive['low'] & social['low'] & emotional['low'] & spiritual['med'] & physical['low'],output['vhigh'])
rule4=ctrl.Rule(cognitive['low'] & social['low'] & emotional['med'] & spiritual['low'] & physical['low'],output['vhigh'])
rule5=ctrl.Rule(cognitive['low'] & social['med'] & emotional['low'] & spiritual['low'] & physical['low'],output['vhigh'])
rule6=ctrl.Rule(cognitive['med'] & social['low'] & emotional['low'] & spiritual['low'] & physical['low'],output['vhigh'])
rule7=ctrl.Rule(cognitive['low'] & social['low'] & emotional['low'] & spiritual['med'] & physical['med'],output['high'])
rule8=ctrl.Rule(cognitive['low'] & social['low'] & emotional['med'] & spiritual['low'] & physical['med'],output['high'])
rule9=ctrl.Rule(cognitive['low'] & social['med'] & emotional['low'] & spiritual['low'] & physical['med'],output['high'])
rule10=ctrl.Rule(cognitive['med'] & social['low'] & emotional['low'] & spiritual['low'] & physical['med'],output['high'])
rule11=ctrl.Rule(cognitive['low'] & social['low'] & emotional['med'] & spiritual['med'] & physical['low'],output['high'])
rule12=ctrl.Rule(cognitive['low'] & social['med'] & emotional['low'] & spiritual['med'] & physical['low'],output['high'])
rule13=ctrl.Rule(cognitive['med'] & social['low'] & emotional['low'] & spiritual['med'] & physical['low'],output['high'])
rule14=ctrl.Rule(cognitive['low'] & social['med'] & emotional['med'] & spiritual['low'] & physical['low'],output['high'])
rule15=ctrl.Rule(cognitive['med'] & social['low'] & emotional['med'] & spiritual['low'] & physical['low'],output['high'])
rule16=ctrl.Rule(cognitive['med'] & social['med'] & emotional['low'] & spiritual['low'] & physical['low'],output['high'])
rule17=ctrl.Rule(cognitive['low'] & social['low'] & emotional['med'] & spiritual['med'] & physical['med'],output['med'])
rule18=ctrl.Rule(cognitive['low'] & social['med'] & emotional['med'] & spiritual['med'] & physical['low'],output['med'])
rule19=ctrl.Rule(cognitive['med'] & social['med'] & emotional['med'] & spiritual['low'] & physical['low'],output['med'])
rule20=ctrl.Rule(cognitive['med'] & social['med'] & emotional['med'] & spiritual['med'] & physical['low'],output['med'])
rule21=ctrl.Rule(cognitive['med'] & social['med'] & emotional['med'] & spiritual['low'] & physical['med'],output['med'])
rule22=ctrl.Rule(cognitive['med'] & social['med'] & emotional['med'] & spiritual['low'] & physical['med'],output['med'])
rule23=ctrl.Rule(cognitive['med'] & social['med'] & emotional['med'] & spiritual['med'] & physical['med'],output['med'])
rule24=ctrl.Rule(cognitive['med'] & social['med'] & emotional['med'] & spiritual['med'] & physical['high'],output['low'])
rule25=ctrl.Rule(cognitive['med'] & social['med'] & emotional['med'] & spiritual['high'] & physical['med'],output['low'])
rule26=ctrl.Rule(cognitive['med'] & social['med'] & emotional['high'] & spiritual['med'] & physical['med'],output['low'])
rule27=ctrl.Rule(cognitive['med'] & social['high'] & emotional['med'] & spiritual['med'] & physical['med'],output['low'])
rule28=ctrl.Rule(cognitive['high'] & social['med'] & emotional['med'] & spiritual['med'] & physical['med'],output['low'])
rule29=ctrl.Rule(cognitive['low'] & social['low'] & emotional['low'] & spiritual['high'] & physical['high'],output['low'])
rule30=ctrl.Rule(cognitive['low'] & social['low'] & emotional['high'] & spiritual['med'] & physical['high'],output['low'])
rule31=ctrl.Rule(cognitive['low'] & social['high'] & emotional['low'] & spiritual['low'] & physical['high'],output['low'])
rule32=ctrl.Rule(cognitive['high'] & social['low'] & emotional['low'] & spiritual['low'] & physical['high'],output['low'])
rule33=ctrl.Rule(cognitive['low'] & social['low'] & emotional['high'] & spiritual['high'] & physical['low'],output['low'])
rule34=ctrl.Rule(cognitive['low'] & social['high'] & emotional['low'] & spiritual['high'] & physical['low'],output['low'])
rule35=ctrl.Rule(cognitive['high'] & social['low'] & emotional['low'] & spiritual['high'] & physical['low'],output['low'])
rule36=ctrl.Rule(cognitive['high'] & social['low'] & emotional['high'] & spiritual['low'] & physical['low'],output['low'])
rule37=ctrl.Rule(cognitive['low'] & social['high'] & emotional['high'] & spiritual['low'] & physical['low'],output['low'])
rule38=ctrl.Rule(cognitive['high'] & social['high'] & emotional['low'] & spiritual['low'] & physical['med'],output['low'])
rule39=ctrl.Rule(cognitive['high'] & social['high'] & emotional['low'] & spiritual['med'] & physical['med'],output['low'])
rule40=ctrl.Rule(cognitive['high'] & social['high'] & emotional['med'] & spiritual['low'] & physical['low'],output['low'])



#pass the value to ControlSystem and Simulate before calculating actual output.
output_calc = cts.ControlSystem([rule1,rule2,rule3,rule4,rule5,rule6,rule7,rule8,rule9,rule10,rule11,rule12,rule13,rule14,rule15,rule16,rule17,rule18,rule19,rule20,rule21,rule22,rule23,rule24,rule25,rule26,
                                 rule27,rule28,rule29,rule30,rule31,rule32,rule33,rule34,rule35,rule36,rule37,rule38,rule39,rule40])
cog = cts.ControlSystemSimulation(output_calc)
#Now pass input as
cog.input['cognitive']=30
cog.input['social']=20
cog.input['emotional']=20
cog.input['spiritual']=30
cog.input['physical']=20
cog.compute() #calculate cgpa
print(cog.output['output']) #print calculated cgpa
output.view(sim=cog) #visualize output
plt.show()