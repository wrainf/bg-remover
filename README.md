# Automatic Background Remover
Simple application that allows you to automatically remove the backgroun of an image. This is split into two components, client and server. Client handles getting custom images to upload. Backend receives images, feeds it to background remover, and sends back the result.

Feel free to create a PR to add more features!

## Installation
1. Clone this repo
   
## Frontend
### Start
Simple static site just open index.html in your browser.

## Backend
### Initialisation
1. CD into server/ : `cd server`
2. Install dependencies: `pip install backgroundremover && pip install flask && pip install flask-cors`
3. Setup backgroundremover: `backgroundremover -i 'image.png' -o 'output.png'`
### Start
1. Run: `flask --ap index run`
2. Running on `localhost:5000`
