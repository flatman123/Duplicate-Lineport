#! /usr/bin/python4

import csv, re
import subprocess, time

line_counter = 0
header_cnt = 0

headers = [
        "Enterprise ID", " Group ID"," Device Name",
        " Device Type", " UCount"," Line Ports",
        " New DName"," New DType"," User Agent"
        ]

def my_timer(func):
    def timer_wrapper():
        t1 = time.time()
        func()
        t2 = time.time()
        print(f"Function {func.__name__} took {round(t2 - t1, 2)} seconds to run.")
    return timer_wrapper

    

@my_timer   
def ftp_chker():
    '''READS LINEPORTS FROM FILE and OUTPUTS TO SEPARATE FILE.
        >>> "6548468138@"  OUTPUT TO LINEPORT.TXT'''
    original_file = "<YOUR CSV FILE HERE>"
    output_lineport_file = "<YOUR CSV FILE HERE>"

    with open(output_lineport_file, "r") as lineport_file:
        contents = csv.DictReader(lineport_file)
        for line in contents:
            pattern = re.compile(r"\d+@")
            lineport_match = pattern.finditer(line[" Line Ports"])
            
            # EXTRACTS THE LINEPORTS FROM THE CSV-FILE BASED ON REGEX MATCHINGS
            for lineport in lineport_match:
                grepping = [f"grep -P '{lineport.group(0)}' <YOUR CSV FILE HERE> >> LINEPORT_OUT.txt"]
                print(lineport.group(0))
                line_counter += 1

                with open("lineport.txt", "a") as lineportfile:
                    content = lineportfile.write(lineport.group(0) + "\n")
                CALL_BASH_SCRIPT = subprocess.call(grepping, shell=True)
    print(f"There are {line_counter} lines in this file")
    return 



def write_duplicate_entries(args):
    global header_cnt
    duplicate_headers = ["Enterprise ID", " Device Name", " Line Ports"]
    print(args)
    with open("DUPLICATE_LINEPORTS.txt", "a", newline="") as file:

        #THE COMMENTED OUT SECTION IS FOR WRITING AS CSV
        # csv_writer = csv.DictWriter(file, fieldnames=duplicate_headers, delimiter=",")
        
##        if header_cnt != 0:
##            csv_writer.writeheader()
##            header_cnt += 1
##        else:
##            pass
##        csv_writer.writerow(args)
        file.write(args + "\n")
     return


def lineport_chker():
        '''CHECKS FOR MATCHED FIELDS IN CSV FILE, WRITES MATCHED
        VALUES TO A NEW CSV FILE'''
    lineport_counter = 0
    lineport = ""
    restart_loop = True # 2nd while loop WILL NOT RUN TWICE, SO A "RESTART" VARIABLE WAS CREATED TO FORCE THE
    loop_1 = 0
    
    while loop_1 < 100:
       with open("lineport.txt","r") as lp_file:
            lineport_file = lp_file.readlines()

            for x in lineport_file:
                lineport_file
                lineport = x.strip()     
                print(x)

                while restart_loop:
                    restart_loop = False
                    with open("<YOUR CSV FILE HERE>", "r", newline="") as ftp_file:
                        csv_reader = csv.DictReader(ftp_file, fieldnames=headers, delimiter=",")

                        for csv_line in csv_reader:
                            print(lineport + " IN " + csv_line[" Line Ports"])
                            #time.sleep(1)
                            if lineport in csv_line[" Line Ports"]:
                                lineport_counter += 1

                            # ONLY WRITE TO DUPLICATE FILE IF MORE THEN ONE ENTRY IS FOUND
                                if lineport_counter > 1:
                                    duplicate = csv_line["Enterprise ID"] + "," +\
                                                csv_line[" Device Name"] + "," +\
                                                csv_line[" Line Ports"].strip(",")
                                    write_duplicate_entries(duplicate)
                            else:
                                pass
                    lineport_counter = 0        
                    restart_loop = True
                    break
                else:
                    #RESETS THE LINEPORT COUNTER
                    lineport_counter = 0
                    pass
            loop_1 += 1
    return

if __name__ == "__main__":
    #ftp_chker()
    lineport_chker()
