from biosppy.signals import ecg

def preprocessing():
    patients = []
    input = open('upd_records.txt', 'r')
    for line in input:
        line = line.replace("\n","")
        arr = line.split('/')
        record2 = wfdb.rdrecord(arr[1], pb_dir='ptbdb/' + arr[0] + '/', channels=[1,2,5])	
        f = open('data.txt', 'w')
        f.write("# Simple Text Format\n")
        f.write("# Sampling Rate (Hz):= 1000.00\n")
        f.write("# Resolution:= 12\n")
        f.write("# Labels:= ECG\n")
        print(np.array(record2.p_signal).shape)
        for x in record2.p_signal:
            f.write(str(x[0]) + " " + str(x[1]) + " " + str(x[2]) + "\n")
        f.close()
        xxxs = ""
        xxx = open("data.txt")
        s=xxx.readlines()[4:]
        signal0 = np.loadtxt("data.txt", usecols = (0))
        out0 = ecg.ecg(signal=signal0, sampling_rate=1000., show = False)["templates"]
        signal1 = np.loadtxt("data.txt", usecols = (1))
        out1 = ecg.ecg(signal=signal1, sampling_rate=1000., show = False)["templates"]
        signal2 = np.loadtxt("data.txt", usecols = (2))
        out2 = ecg.ecg(signal=signal2, sampling_rate=1000., show = False)["templates"]
        ff = open('temp.txt','w')
        average_signal = []
        for x in range(len(out0[0])):
            average_signal.append(sum(out0[:,x])/len(out0[:,x]))
        for x in range(len(out1[0])):
        	average_signal.append(sum(out1[:,x])/len(out1[:,x]))
        for x in range(len(out2[0])):
       		average_signal.append(sum(out2[:,x])/len(out2[:,x]))
        for i in range(len(average_signal)):
            ff.write(str(average_signal[i])+ "\n")
        ff.close()
        time = [i for i in range(1, 1801)]
        load_data = np.array(average_signal)
        patients.append(load_data)
    output = open('result_data.txt','w')
    output.write("\n".join([",".join([str(x) for x in np_arr.tolist()]) for np_arr in patients]))
    output.close()