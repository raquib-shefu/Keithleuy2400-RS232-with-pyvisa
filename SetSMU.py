import visa
# import numpy as np
import time as t
from pyvisa.constants import SerialTermination

reading = 20
rm = visa.ResourceManager()
print(rm.list_resources())
smu = rm.open_resource('ASRL21::INSTR')
del smu.timeout
smu.read_termination = '\r'
print(smu.end_input)
smu.end_input = SerialTermination.termination_char
# smu.write_termination = '\r'+'\n'
smu.write('*IDN?')
data = smu.read_bytes(80, smu.end_input)
print(data)
def smu_setting():
    smu.write('*RST')
    smu.write(':SOUR:FUNC:MODE VOLT')
    smu.write(':SOUR:LIST:VOLT 5')
    smu.write(':ARM:COUNT 1')
    smu.write('TRIG:COUN ' + str(reading))  # %maximum 2500
    smu.write(':TRIG:DEL 0.0')
    smu.write(':SOUR:DEL 0.0')
    smu.write(':SOUR:VOLT:RANGE 1')
    smu.write(':SENSE:CURR:PROT 100e-3')
    smu.write(':SENSE:FUNC:CONC OFF')
    smu.write(':SENSE:FUNC "CURR:DC"')
    smu.write(':SENSE:CURR:RANGE 1e-3')
    smu.write(':SENSE:CURR:NPLC 0.01')
    smu.write(':SENSE:AVERAGE:STAT OFF')
    # smu.write(':DISP:ENAB OFF')
    smu.write(':SYSTEM:AZERO:STAT OFF')
    smu.write(':TRAC:CLE')
    smu.write(':TRAC:POINTS ' + str(reading))  # %max 2500
    smu.write(':TRAC:FEED SENSE1')
    smu.write(':SOUR:VOLT:MODE LIST')
    smu.write(':TRAC:FEED:CONT NEXT')
    smu.write(':OUTPUT ON')


def smu_measure():
    smu.write(':INIT')
    t.sleep(5)


def smu_read():
    smu.write(':FORM:ELEM CURR,TIME')
    smu.write("trace:data?")
    s1 = ''
    for i in range(1, 7, 1):
        s = smu.read_bytes(1)
        print(s)
        s1 = s1 + (s.decode("utf-8"))[1:]
    s2 = smu.read()
    s3 = (s1 + s2)
    print(s3)
    fd = open('SMU_reading_{}.txt'.format(reading), 'w')
    fd.write(s3)
    fd.close()
    smu.write("trace:clear; feed:control next")



# smu.write(':INIT')
# t.sleep(2)
# smu.write(':FORM:ELEM CURR,TIME')
# smu.write("trace:data?")
# print(smu.read_bytes(60))
#
#
# smu.write(':OUTPUT OFF')
# def smureading(smu):
#     smu.write(':INIT')
#     t.sleep(2)
#     smu.write(':FORM:ELEM CURR,TIME')
#     smu.write("trace:data?")
#     print(smu.read_bytes(60))
#     # print('sleeping')
#
#     # smu.write("trace:clear; feed:control next")
#     # smu.write(':INIT')
#     # smu.write(':FORM:ELEM CURR,TIME')
#     # smu.write("trace:data?")
#     # print(smu.read_ascii_values())
#
#     # print(smu.read_bytes(3000))
#
#     # voltages = smu.query_ascii_values("trace:data?")
#     # print("Average voltage: ", sum(voltages) / len(voltages))
#     # # print(I)
#     # smu.query("status:measurement?")
#     # smu.write("trace:clear; feed:control next")
#     # print(smu.read_bytes(10))
#     # print(smu.read_bytes(10))
#     # print(smu.read_bytes(10))
#
#
# def smucalculation():

# smu.write(':OUTPUT OFF')
