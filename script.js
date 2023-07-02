const form = document.getElementById("imageForm")
const resultContainer = document.getElementById('result')
const loader = document.getElementById('loading')
const baseURL = "https://auto-bg-remover.onrender.com"
let imageID;
let imageURL;
let interval;
form.addEventListener('submit', async function(event) {
  event.preventDefault()
  loader.className = 'loading-container'
  const formData = new FormData(form)
  const res = await fetch(`${baseURL}/upload`, {method: 'POST', body: formData})
  const json = await res.json()
  imageID = json.id
  interval = setInterval(getImage, 5000);
})

async function getImage(){
  const res = await fetch(`${baseURL}/fetch/${imageID}`);
  if(res.ok){
    const blob = await res.blob()
    if(blob.size > 0) {
      imageURL = await URL.createObjectURL(blob)
      console.log(imageURL);
      const imageElement = document.createElement('img');
      imageElement.src = imageURL;
      resultContainer.prepend(imageElement);
      clearInterval(interval)
      loader.className = 'hidden'
    }
    
  } else {
    alert("Image processing failed")
  }
  
}

resultContainer.addEventListener('click', function() {
  const link = document.createElement('a')
  if(imageURL) {
    link.href = imageURL
    link.download = 'image_bg.png'
    link.click()
    link.remove()
  }
})
