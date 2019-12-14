# Do not edit this file or it may not load correctly
# if you try to open it with the RSG Dialog Builder.

# Note: thisDir is defined by the Activator class when
#       this file gets exec'd

from rsg.rsgGui import *
from abaqusConstants import INTEGER, FLOAT
dialogBox = RsgDialog(title='UEL\xb1\xe3\xbd\xdd\xcc\xe1\xbd\xbb\xb2\xe5\xbc\xfe', kernelModule='uel', kernelFunction='uel', includeApplyBtn=True, includeSeparator=True, okBtnText='OK', applyBtnText='Apply', execDir=thisDir)
RsgLabel(p='DialogBox', text='\xb1\xb8\xd7\xa2\xa3\xbaCOHEELEM-0ALL\xd2\xaa\xb8\xc4\xb3\xc9CO_SET', useBoldFont=True)
RsgHorizontalFrame(name='HFrame_5', p='DialogBox', layout='0', pl=0, pr=0, pt=0, pb=0)
RsgCheckButton(p='HFrame_5', text='UEL\xc4\xa3\xca\xbd', keyword='uel_mode', default=True)
RsgHorizontalFrame(name='HFrame_6', p='HFrame_5', layout='0', pl=50, pr=0, pt=0, pb=0)
RsgCheckButton(p='HFrame_5', text='\xbd\xbb\xbb\xa5\r', keyword='interactive', default=False)
RsgComboBox(name='ComboBox_4', p='DialogBox', text='Part:', keyword='partName', default='', comboType='MDB', repository='parts', rootText='Model:', rootKeyword='modelName', layout='HORIZONTAL')
RsgFileTextField(p='DialogBox', ncols=25, labelText='File name:', keyword='fileName', default='C:/temp/UEL/cohesive_uel.for', patterns='(*.for)')
RsgSeparator(p='DialogBox')
RsgGroupBox(name='GroupBox_2', p='DialogBox', text='\xb2\xce\xca\xfd', layout='LAYOUT_FILL_X')
RsgHorizontalFrame(name='HFrame_7', p='GroupBox_2', layout='0', pl=0, pr=0, pt=0, pb=0)
RsgTextField(p='HFrame_7', fieldType='Float', ncols=8, labelText='En:', keyword='En', default='10000')
RsgHorizontalFrame(name='HFrame_9', p='HFrame_7', layout='0', pl=50, pr=0, pt=0, pb=0)
RsgTextField(p='HFrame_9', fieldType='Float', ncols=8, labelText='Es:', keyword='Es', default='10000')
RsgHorizontalFrame(name='HFrame_8', p='GroupBox_2', layout='0', pl=0, pr=0, pt=0, pb=0)
RsgTextField(p='HFrame_8', fieldType='Float', ncols=8, labelText=' tn:', keyword='tn', default='2.65')
RsgHorizontalFrame(name='HFrame_10', p='HFrame_8', layout='0', pl=50, pr=0, pt=0, pb=0)
RsgTextField(p='HFrame_10', fieldType='Float', ncols=8, labelText=' ts:', keyword='ts', default='2.65')
RsgHorizontalFrame(name='HFrame_11', p='GroupBox_2', layout='0', pl=-3, pr=0, pt=0, pb=0)
RsgTextField(p='HFrame_11', fieldType='Float', ncols=8, labelText='Gf1:', keyword='Gf1', default='0.18')
RsgHorizontalFrame(name='HFrame_12', p='HFrame_11', layout='0', pl=42, pr=0, pt=0, pb=0)
RsgTextField(p='HFrame_12', fieldType='Float', ncols=8, labelText='Gf2:', keyword='Gf2', default='0.18')
RsgTextField(p='GroupBox_2', fieldType='Float', ncols=5, labelText='Initial thickness:', keyword='ini_thick', default='1')
RsgTextField(p='GroupBox_2', fieldType='Float', ncols=5, labelText='Outpl thickness:', keyword='out_thick', default='1')
RsgComboBox(name='ComboBox_6', p='GroupBox_2', text='constitutive', keyword='constitutive', default='exponent', comboType='STANDARD', repository='', rootText='', rootKeyword=None, layout='')
RsgListItem(p='ComboBox_6', text='customize')
RsgListItem(p='ComboBox_6', text='exponent')
RsgListItem(p='ComboBox_6', text='Linear')
RsgListItem(p='ComboBox_6', text='CEB')
RsgListItem(p='ComboBox_6', text='Roesler')
RsgListItem(p='ComboBox_6', text='Petersson')
RsgGroupBox(name='GroupBox_3', p='GroupBox_2', text='CPU', layout='LAYOUT_FILL_X')
RsgVerticalFrame(name='VFrame_1', p='GroupBox_3', layout='0', pl=40, pr=0, pt=0, pb=0)
RsgSlider(p='VFrame_1', text='', minLabelText='Min', maxLabelText='Max', valueType=INTEGER, minValue=1, maxValue=4, decimalPlaces=1, showValue=True, width=200, keyword='cpus', default=1)
RsgHorizontalFrame(name='HFrame_4', p='GroupBox_3', layout='0', pl=0, pr=0, pt=0, pb=20)
dialogBox.show()