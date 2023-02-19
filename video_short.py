from datetime import datetime
from moviepy.editor import *
from moviepy.audio import *
import selenium_post
import random
import time as time_mod
import os

#----------------------#
video_folder="video"
music_folder="music"
result_folder="result"
nb_video=10
original_path=str(__file__).split("video_short.py")[0] #Se termine par un /
print("The Path is :",original_path)
#----------------------#


date=str(datetime.now()).split(" ")[0].split("-")
day=int(date[2])+1
month=int(date[1])
year=int(date[0])
hour=10

try: #Evite de sortir 2 fois la meme video si elles n'ont pas toutes été utilisée
    file=open("video.txt")
    use_video=file.read().split("\n")
    file.close()
except:
    use_video=[]

def my_random(begin,end):
    nb1 = int(random.randint(0,end)**(begin%10))
    nb2 = int(time_mod.time()*10)
    nb3 = random.randint(0,12006)%17
    try:
        nb4 = int(os.statvfs('/')[3])
    except:
        nb4 = 1234567
    #print(nb1, nb2, nb3, nb4)
    result = int(((nb1+nb2+nb3+nb4+random.randint(0,10000))%(end-begin+1))+begin)
    return result

#Test De ma fonction random
"""
r={}
for i in range(100000):
    nb=my_random(40,50)
    try:
        idx = r[str(nb)]
        r[str(nb)] = idx + 1
    except:
        r[str(nb)] = 1
print(r)
"""

#video_to_youtube.upload_video(f"result/clip_9.mp4",f"Exploration --- Clip_9.mp4","",["France"],year,month,day,hour,1,1)
for i in range(nb_video):
    try:
        max_time=my_random(20,55)

        find_not_use=False
        for i in os.listdir(video_folder):
            if str(i)[0] != ".":
                if i not in use_video:
                    find_not_use=True
        if not find_not_use:
            use_video=[]
        print("Use Video :",use_video)

        name_v = "."
        t=0
        while name_v[0] == "." or name_v in use_video:
            if t >500:
                break
            name_v = random.choice(os.listdir(video_folder))
            t+=1
        use_video.append(name_v)
        print("Use Video :",use_video)

        file=open("video.txt","w")
        file.write("\n".join(use_video))
        file.close()

        video = video_folder + "/" + name_v
        print("\n\nVideo :",video)
        clip_original = VideoFileClip(video)
        clip_original_duration = clip_original.duration
        print("Duration :", clip_original_duration)


        name_m = "."
        while name_m[0] == ".":
            name_m = random.choice(os.listdir(music_folder))
        music = music_folder + "/" + name_m
        print("Music :",music)
        audio_original = AudioFileClip(music)
        print("Duration : ",audio_original.duration)

        if audio_original.duration > max_time:
            time=max_time
            start=my_random(0,int(audio_original.duration-max_time-1))
            print("Audio Start :",start)
            audio_final=audio_original.subclip(start,start+max_time)
        else:
            print("Audio Start at the begining")
            time=int(audio_original.duration)
            audio_final=audio_original

        time_cut=[]
        tt=time
        while tt>0:
            time_cut.append(my_random(3,(tt%14+3)))
            tt-=time_cut[-1]
        if tt<0:
            time_cut[-1]=time_cut[-1]+tt
        print("Découpage Plan (second) :",time_cut)


        result_clips = [] #[Clip1 obj, Clip2 obj]
        second_use = [] #[time1, time2] Contient toutes les secondes du clip original qui sont utilisées
        for time in time_cut:
            find=False
            tour_re=0
            while not find:
                find=True
                start = my_random(0,(int(clip_original_duration)-(time+1)))    
                for i in range(0,(time+1)):
                    if int(start+i) in second_use:
                        find=False
                if tour_re>1000:
                    print("Erreur Bénine : des morceaux seront en double")
                    find=True
                tour_re+=1
            for i in range(0, (time+1)):
                second_use.append(int(start+i))
            end = start+time
            print("Séquence from " + str(start) + "s to " + str(end) + "s")

            clip = clip_original.subclip(start, end)
            result_clips.append(clip)
            
        print(result_clips)

        final_clip = concatenate_videoclips(result_clips)
        final_clip = final_clip.set_audio(audio_final)

        name="clip_0.mp4"
        number=0
        ls=os.listdir(result_folder)
        while name in ls :
            number+=1
            name="clip_"+str(number)+".mp4"
        print("Result name :",name)

        #final_clip.write_videofile(f"{result_folder}/{name}", fps=30, threads=10, codec="libx264")

        print("TikTok Resizing")
        tiktok_clip = final_clip.resize(height=1920)
        middle_x = int(tiktok_clip.size[1]/2)
        x1_tiktok = int(middle_x-540)
        x2_tiktok = int(middle_x+540)
        tiktok_clip = tiktok_clip.crop(x1=x1_tiktok, y1=0, x2=x2_tiktok, y2=1920)

        print("Saving...\n\n")
        tiktok_clip.write_videofile(f"{result_folder}/{name}", fps=30, threads=12, codec="libx264")
        print("\n\nSucces :",f"{result_folder}/{name}")
        
        print("Scheedule Upload on Youtube")
        hour+=1
        if hour > 14:
            hour=1
            day+=1
        if day>28:
            day=1
            month+=1
        if month>12:
            month=1
            year+=1
        
        print("FILE :",f"{original_path}{result_folder}/{name}")
        
        try:
            print("POST YOUTUBE")
            selenium_post.start_youtube(f"{original_path}{result_folder}/{name}",f"Urbex Exploration --- {name}","Exploration Urbaine #Urbex","Urbex, GrandEst, Exploration",str(day),str(month),str(year),str(hour),"01")
        except:
            print("ERR : Post Youtube")
        time_mod.sleep(35)
        
        try:
            print("POST TIKTOK")
            selenium_post.start_tiktok(f"{original_path}{result_folder}/{name}",f"Urbex Exploration --- {name}","#Urbex #GrandEst #Exploration")
        except:
            print("ERR : Post tiktok")
        time_mod.sleep(35)
        print("POST INSTAGRAM")
        try:
            selenium_post.start_instagram(f"{original_path}{result_folder}/{name}",f"Urbex Exploration --- {name}\n#urbex #monde #abandoned #urbex #urbexfrance #abandonedplaces #urbexworld #france #lostplaces #urbanexploration #urbexpeople #urbexplaces #urbanexplorer #urban #exploration #forgotten #ruins #lost")
        except:
            print("ERR : Post tiktok")
        #video_to_youtube.upload_video(f"{result_folder}/{name}",f"Exploration --- {name}","",["France"],year,month,day,hour,1,1)
    except Exception as e:
        print("--- An Error occure ---")
        print(repr(e))
        print("But A new video is about to be generate !")
