# DailyHunt-NewsAPI [Unofficial]

---

An Unofficial Daily Hunt API Which Fetches News from Daily Hunt .

---

## News Categories 

---

1. science

2. technology

3. india (Indian News)

4. automobile

5. entertainment 

6. sport 

7. world

8. lifestyle

9. employment

10. religion

11. movies

12. football


---
## Usage

Make a get request specifying the category of news you want
```
https://dailyhunt.herokuapp.com/news?category={category_name}
```
Example - https://dailyhunt.herokuapp.com/news?category=science

---

## Response Format 

Example Of Daily Hunt API Response Below 

--- 

```JSON

{
  "data": [
    {
      "PublishedTime": "2020-05-31 17:03:00",
      "content": "If we believe the legends, then Intel produced a Core i5-7660X processor 3 years ago but never officially released it. However, there are times when legends turn out to be reality. A Chinese Twitter user by the username \ni5-7660Ｘ，the only i5 with quad channel memory support and 28 pci-e lanes,because it’s a Skylake-X cpu Spec: 6C6Tup to 5Ghz4channel ddr428 pci-e lanessupport AVX512 @momomo_us @_rogame pic.twitter.com/79KMBJ9C0q\n posted images of a working sample of the processor which belongs to the Skylake-X family on May 27, 2020.\ni5-7660Ｘ，the only i5 with quad channel memory support and 28 pci-e lanes,because it's a Skylake-X cpu Spec: 6C6Tup to 5Ghz4channel ddr428 pci-e lanessupport AVX512 @momomo_us @_rogame pic.twitter.com/79KMBJ9C0q \nAs the images suggest, the processor, without a doubt uses Skylake micro-architecture.",
      "imageUrl": "http://assets-news-bcdn.dailyhunt.in/cmd/resize/400x400_80/fetchdata16/images/2e/a4/cb/2ea4cb5293bb90651119e9f6504ced8a32be168d9d246259a4cc2615f220b633.jpg",
      "publisherStory": "https://www.techquila.co.in/a-legend-comes-to-life-mythical-intel-processor-found",
      "title": "A Legend Comes to Life: Mythical Intel Processor Found",
      "url": "http://dhunt.in/9PC9u",
      "viewCount": "1.9k"
    },
    {
      "PublishedTime": "2020-05-31 17:03:00",
      "content": "MSI is expanding the hardware possibilities for its users. It is all set to launch a new Gaming monitor specially designed for eSports. MSI has announced Optix MAG274R which is an IPS eSports Gaming Monitor. The monitor is equipped with an IPS panel and features a 144 Hz refresh rate and a 27' display. It has a fast response time of 1ms. MSI has claimed that the users will enjoy the best viewing experience. For gamers, its a delight as the company has claimed that they will enjoy the smoothest gaming experience. The monitor has a resolution of 1920 x 1080 and it is designed for competitive gamers.",
      "imageUrl": "http://assets-news-bcdn.dailyhunt.in/cmd/resize/400x400_80/fetchdata16/images/aa/21/c1/aa21c1641a0f3621b14d49b4454d8207eae4b2b3b099baf4817f68e3de200426.jpg",
      "publisherStory": "https://www.techquila.co.in/msis-gaming-monitor-is-here-designed-for-esports",
      "title": "MSI's Gaming Monitor is Here: Designed For eSports",
      "url": "http://dhunt.in/9PC7W",
      "viewCount": "1.7k"
    }
}

```

---
## Setup

Install all dependencies listed in *requirements.txt* file. 

1. To install all dependencies run - 

    ```bash
    $ sudo -H pip3 install -r requirements.txt
    ```

2. Start the server

    ```bash 
    $ python app.py
    ```
---

---

### You can fork the repo and deploy on VPS or deploy it on Heroku :)  
[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/Gowtham2003/Inshorts-News-API/tree/master)

---




