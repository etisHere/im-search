from time import sleep
import os

#Taking the name of the movie and adding the search link
x = input("Name of movie: ")

#This will join any spaces together with %20
output_one = x.split(" ")
output_two = "%20".join(output_one)

#Joined link
output_join = f""" "https://www.imdb.com/find/?q={output_two}&ref_=nv_sr_sm" """ 

#grep -oP '(?<=class="sc-466bb6c-0 hlbAws">)[^<]+'

#Curling the output from above/find the correct ext and adding it to temp for a new link.(grep is searching for everything inside 'title/' and awk is printing the second line as first is some garbage we don't need. 
y = os.system(f"""curl -A "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36" {output_join}  | grep -Eo 'title/[^"]+"' | awk 'NR==2' > weblink_tmp""")
#Calling the system again to just remove text(called twice for later ref as the first sed call the text is actually needed later
os.system(f"""curl -A "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36" {output_join}  | grep -Eo 'title/[^"]+"' | awk 'NR==2' > weblink_tmp_two""")
os.system("sed -i 's/?ref_=fn_al_tt_1//g' weblink_tmp")
os.system("""sed -i 's/"//g' weblink_tmp""")
os.system("""sed -i 's/"//g' weblink_tmp_two""")

#Taking the link from above and making a new link
with open('weblink_tmp', 'r') as file:
    # Read the contents of the file and then removing any new lines(without "replace" the text_content goes to the second line.)
    text_content = file.read().replace("\n", "")

#Grabing info from other tmp file
with open('weblink_tmp_two', 'r') as file:
    text_two = file.read().replace("\n", "")


text = "ratings/?ref_=tt_ov_rt"
new_link = f"https://www.imdb.com/{text_content}{text}" 
new_link_two = f"https://www.imdb.com/{text_two}" 
print(new_link_two)
print(new_link)


#Now Finally gathering the rating info

os.system(f"""curl -A "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36" {new_link_two} > temp_two""")
sleep(2)
os.system(f"""curl -A "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36" {new_link} > temp""")
os.system("clear")
print("Gathering info..")
print("******************")
print("RATING:")
with open('temp', 'r') as file:
    text_con = file.read()

#print(text_con)
os.system(f"""cat temp | grep -oP '(?<=<span class="sc-5931bdee-1 gVydpF">)[^<]+'""")

print("INFO:")
os.system(f"""cat temp_two | grep -oP '(?<=class="sc-466bb6c-0 hlbAws">)[^<]+'""")

print("******************")
