import os, subprocess
# These Next 3 Lines are setup - so I'm assuming they don't count in the 15 line limit.
POTHOLE_REQ = "http://seshat.datasd.org/get_it_done_311/get_it_done_pothole_requests_datasd.csv"
GRAF_REQ = "http://seshat.datasd.org/get_it_done_311/get_it_done_graffiti_removal_requests_datasd.csv"
DOWNLOADS_DIR = "{}/temp".format(os.getcwd())
FINAL_FILE = "{}/all_requests.csv".format(os.getcwd())

# Create directory if not exists
if not (os.path.exists(DOWNLOADS_DIR)):
    os.mkdir(DOWNLOADS_DIR)

subprocess.check_call(["wget", GRAF_REQ, "-O", "{}/graffiti_req.csv".format(DOWNLOADS_DIR)])
subprocess.check_call(["wget", POTHOLE_REQ, "-O", "{}/pothole_req.csv".format(DOWNLOADS_DIR)])
final_file = open(FINAL_FILE, 'w')

for f in os.listdir(DOWNLOADS_DIR):
    filepath = "{}/{}".format(DOWNLOADS_DIR, f)
    output = subprocess.check_output(["cut", "-d", ",", "-f", "1,2,4,7", filepath]).decode('utf-8')
    final_file.write(output);
    os.remove(filepath)

final_file.close()
number_of_lines = subprocess.check_output(["wc", "-l", FINAL_FILE]).decode('utf-8')
print("Number of lines in all requests is {}".format(number_of_lines))

