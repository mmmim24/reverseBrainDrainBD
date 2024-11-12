from bs4 import BeautifulSoup
import requests
import json
html_doc = []
object = {}
url =  "https://we.reversebraindrainbd.com/details/"

def main():
    for i in range(1 , 525):
        print(i,end=" ")
        response = requests.get(url+str(i))
        soup = BeautifulSoup(response.text, 'html.parser')
        nf = soup.find('div', class_='ml-4 text-lg text-gray-500 uppercase tracking-wider')
        if nf is not None:
            print(nf.text.strip())
        else:
            print("Found")
            rbd = soup.find('div', class_='container my-10 mx-auto p-4')
            name = rbd.find('h2', class_='card-title text-md')
            place = rbd.find_all('h1', class_='flex items-center my-2')
            field = rbd.find_all('h1', class_='py-2')
            
            fb  = rbd.find('div', class_='flex gap-3')
            if fb and fb.find('a'):
                fb = fb.find('a')['href']
            else:
                fb = "Not Found"
            
            
            post = rbd.find_all('div', class_='card shadow-xl bg-base-100 p-4 my-4')
            if len(post) > 2 and post[2].find('a'):
                post = post[2].find('a')['href']
            else:
                post = "Not Found"
        
        
            object['id'] = i
            object['name'] = name.text
            places = ""
            for i in place:
                places += i.text.strip()+", "
            object['experiences'] = places
            object['description'] = field[0].text
            object['field of interest'] = field[1].text
            object['area of expertise'] = field[2].text
            object['facebook profile'] = fb
            object['facebook post link'] = post
            
            
            # with open("README.md", "a") as file:
            #     for i in object:
            #         file.write(str(i)+": "+str(object[i])+"\n")
            #     file.write("\n")
            #     file.close()
            
            with open("output.txt", "a") as file:
                for i in object:
                    file.write(str(i)+": "+str(object[i])+"\n")
                file.write("\n")
                file.close()

            # with open("output.json", "a") as file:
            #     json.dump(object, file,indent=4)
  
if __name__ == "__main__":
    main()