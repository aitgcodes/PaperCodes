import subprocess
f = open("Region_A.dat", "w")
for i in range(1,282):
        out = subprocess.Popen(["python3","int_cube.py","sqm-wf-st0"+str(f'{i:03}')+".cube","-","-","-"],stdout=subprocess.PIPE,universal_newlines=True)
        out.wait()  # wait until the script has finished
        stdout_data, stderr_data = out.communicate()
        f.writelines(["State  "+str(f'{i:03}')+"  ",stdout_data])
f.close()
