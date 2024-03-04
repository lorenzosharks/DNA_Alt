#The only function in this entire code and it doesn't even matter to the actual part.
def selection():
    
    validAnswer = False
    
    while validAnswer == False:
        option=input('Do you want it in lowercase? Answer "y" for yes and "n" for no: ')
        if option == "y" or option == "n":
            validAnswer = True
        else:
            print("Please enter a valid answer.")
    return option

print("This gives the complementary strand given one half of the DNA.")
print("Capitals doesn't matter. However, the results is in capitals")
print("However, there is a option to change it. Default is in capitals.")
print("")



#Inputs
selection_option = selection()
strand=input("What is half of the strand: ")

#Setting up the code
i=0
result_strand=[]
error = False
dna_strand=list(strand)

#Identifying the length
length=len(dna_strand)

#Actual code
while i<int(length):
    if dna_strand[i]=="t" or dna_strand[i]=="T":
        if selection_option=="n":
            result_strand.append("C")
        if selection_option=="y":
            result_strand.append("c")
    
    elif dna_strand[i]=="c" or dna_strand[i]=="C":
        if selection_option=="n":
            result_strand.append("T")
        if selection_option=="y":
            result_strand.append("t")
    
    elif dna_strand[i]=="a" or dna_strand[i]=="A":
        if selection_option=="n":
            result_strand.append("G")
        if selection_option=="y":
            result_strand.append("g")
    
    elif dna_strand[i]=="g" or dna_strand[i]=="G":
        if selection_option=="n":
            result_strand.append("A")
        if selection_option=="y":
            result_strand.append("a")
    
    else:
        error = True
        break
    i=i+1

if error==False:
    better_strand="".join(result_strand)
    print("")
    print("Result: " + better_strand)
    print("""
I spent way too long on this. Half of the code isn't even for
the main program. Its just for the input options and trying to
get the program to not break every 0.0000001 seconds. Uh, yeah,
thats about it. Oh, and this program is sponsored by nord vpn.
Using my link in the description, you can get a 75% discount and
2 months free. That's only 1.99 a month. Furthermore, nordvpn has
a 30 day money back guarantee so if you are not satisfied, you can
get refunded. In addition, the first 1000 viewers get an additional
3 months free for a total of 5 months free.""")
    print("")
    print("heres the link: https://shorturl.at/sxDHK")
elif error==True:
    print("You have an invalid nucleotide at " + str(i+1) + ".")
    
print("""
this is just so I can claim that I have 100 lines of code in this
program. Its just rants all the way down. Ready for it? Here we go.

Damn the syntax errors! I spent approximately an hour on this program
trying to get it to work and half the time I was just dealing with
syntax errors. Like why do we need a colon after it! There is so much
hassle. Imagine for a second shall we?

You are in a coding streak. You have written over a thousand lines of code
and spent your weekend and life slaving away at mapping textures using C++
and javascript. You finally manage to get your program working. It is a
program to allow fluent modding of Halo Forge. Just as you finish that last
line and run it, a error shows up. It says "Invalid Token at file FHd8&7DHHf"
You stare in horror at that piece of line. That file is generated and is one
of the hundreds in your game file. Finding the file is easy but where the actual
*#($ is the error you think. As you wait for the file finder to find it, you
ponder the reason. Perhaps it is just an indentation error you think to yourself.
However, you also wonder why is the file taking so long. However, you stare in shock
as file FHd8&7DHHf is a 34 gigabyte file. That's why it's taking so long. You momentarily
suffer a heart attack. With apprehension, you open the file. It takes a whopping
15 minutes to open.

You look at the number of lines and you see 760,899,345,920 lines of code. You simply
decide to give up and look for the most common which is misdefinition of string and
floats.

Cut to 4 weeks later.

You find nothing wrong. Your sanity has plunged to an all time low. Your family and
friends are worried about you. You haven't taken a shower in 28 days. Your hair is
long and full of crum. However, you have lowered the possible errors to 700 million
lines of code. Still a lot but less. You decide it's time to put it on reddit. They
are renowned, after all, for solving coding problems. You put the lines of code on
r/coding and wait for results. After taking a shower and getting a decent meal, you
look at your phone. There is a notification from reddit. Your heart pounds as you open
the notification. There was a reply.

A user named "superior_rope_172" says, there is a missing semicolon on line 35,389,279.
You go to that line and see that he indeed is right. After fixing it, you see that
everything is working perfectly fine. The fury inside you rises to a breaking point
as you realize that 2,419,200 seconds of your life has been wasted in a single
semicolon. You declare a digital war on syntax errors and rally the internet. Soon,
a coding revolution breaks out as popular coding languages such as python, java,
javascript, c++, and c# are denounced as the languages of the devil. You laugh upon
your throne as you see languages after languages are toppled to end the evil regime
of syntax errors. Soon, the world returns to the OG coding language of 0s and 1s.

Unbeknownst to you, the programming god is watching from above. He laughs at your
incompetence and watches the circumstances unfold for the 189,317,378,378,378th time.
He is all seeing, the all knowing, and the all syntaxing. He watched as civilizations
after civilizations rose and fell due to his curse of syntax errors. The pyramids were built
by the Ancient Egyptians but they had machines. However, their society collapsed after
one pharoah had enough of syntax errors. He declared coding languages to be banished to
the stones that modern archaeologists now called "hieroglyphics."

A similar fate befell the Ancient Romans. They too had a powerful coding language called
"L.A.T.I.N." This allowed them to operate powerful warmachines, orbital weaponry, and
starships with FTL drives. However, the commander of the Roman Space Force lost 12
Slader-Class battleships (the largest type of Roman battleships to date) to Phoenix A
because of a syntax error. He cracked and set course for Earth. There, he fired his
ship's powerful Magnetically Accelerated Gauss (MAG) guns at Cenibus, Yucatan, Mexico.
Cenibus is the powerhouse of the Roman ecumene that hosts 17 thousand fertile worlds.
However, after the commander fired his MAG guns at Cenibus, it was reduced to a crater
110 miles wide. Soon, he led a brutal and bloody 50 year purge of all planets outside
of Earth. Finally, he reduced Rome's influence to Europe and its power to that of bows
and spears. At last, no traces of Rome's once powerful coding language existed except
on books and walls. Finally at peace, he drove his capital ship, the RSF Juno into
Jupiter. The massive 200 mile long ship with its 500,000 tons of antimatter to fuel
its powerful antimatter engine caused the Great Red Spot on Jupiter.

""")