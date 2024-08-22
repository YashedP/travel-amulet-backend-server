<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/josephHelfenbein/travel-amulet">
    <img src="/public/travelamulet-icon.svg" alt="Logo" width="80" height="80">
  </a>

<h3 align="center">TravelAmulet</h3>

  <p align="center">
    Discover your perfect travel destination with TravelAmulet. Your preferences guide the journey, and AI guides the adventure.
    <br />
    <br />
    <a href="https://travelamulet.vercel.app">Visit</a>
    ·
    <a href="https://github.com/josephHelfenbein/travel-amulet/issues/new?labels=bug&template=bug-report---.md">Report Bug</a>
    ·
    <a href="https://github.com/josephHelfenbein/travel-amulet/issues/new?labels=enhancement&template=feature-request---.md">Request Feature</a>
  </p>
</div>

## About the Project
### To see more about the project visit <a href="https://github.com/josephHelfenbein/travel-amulet">travel-amulet</a>!

### What is this backend server doing?
This server houses the Vector Search API that the main Vercel server is using. Due to the limitation of Vercel, it is impossible to have both NextJS and Python API endpoints in one Vercel server. To combat this impediment, an another Vercel server is used to house the API to take all the metadata filters and find the most similar country and send back the most appropriate country.




### Built With

* [![Flask][Flask]][Flask-url]

### Powered By

* <a href="https://tidbcloud.com/free-trial">TiDB Cloud Serverless</a>
* <a href="https://vercel.com">Vercel</a>


# Getting Started
Here are the steps to run the project locally if you want to develop your own project
## Installation
> **Note: Continues from step 3 on the <a href="https://github.com/josephHelfenbein/travel-amulet">main page</a>
1. Get an openAI API key at [https://openai.com/api](https://openai.com/api)
2. Clone the repo
   ```sh
   git clone https://github.com/YashedP/travel-amulet-backend-server.git
   ```
3. Install the Python Libraries
   ```sh
   pip install -r requirements.txt
   ```
4. Enter your API keys and database URL in a `.env.local' file
   ```js
   DATABASE_URL = "ENTER YOUR DATABASE URL"
   OPENAI_API_KEY = "ENTER YOUR OPENAI API KEY"
   ```
5. You can run the website locally with:
   ```sh
   python 
   ```
   or, if hosting on Vercel, with
   ```sh
   vercel dev
   ```
 
<!-- LICENSE -->
## License

Distributed under the Apache 2.0 License. See `LICENSE.txt` for more information.

<!-- CONTACT -->
## Contact

Joseph Helfenbein - [![LinkedIn][linkedin-shield]][linkedin-url-joseph] - josephhelfenbein@gmail.com

Yash Jani - [![LinkedIn][linkedin-shield]][linkedin-url-yash] - yashjani144@gmail.com

Project Link: [https://github.com/josephHelfenbein/travel-amulet](https://github.com/josephHelfenbein/travel-amulet)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

[Flask]: https://img.shields.io/badge/flask-4590A1?logo=flask&style=for-the-badge&logoColor=white
[Flask-url]: https://flask.palletsprojects.com/en/3.0.x/
[license-shield]: https://img.shields.io/github/license/josephHelfenbein/travel-amulet.svg?style=for-the-badge
[license-url]: https://github.com/josephHelfenbein/travel-amulet/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-0A66C2.svg?style=for-the-badge&logo=linkedin&logoColor=white
[linkedin-url-joseph]: https://linkedin.com/in/joseph-j-helfenbein
[linkedin-url-yash]: https://linkedin.com/in/yash-jani-8245bb26a/
