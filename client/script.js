const form = document.getElementById("imageForm")
const resultContainer = document.getElementById('result')
const loader = document.getElementById('loading')
let imageURL;
form.addEventListener('submit', async function(event) {
  event.preventDefault()
  loading.className = 'loading-container'
  const formData = new FormData(form)
  console.log(formData)
  const res = await fetch('https://bg-remover-h8wh.onrender.com/upload', {method: 'POST', body: formData})
  const blob = await res.blob()
  imageURL = await URL.createObjectURL(blob)
  const imageElement = document.createElement('img');
  imageElement.src = imageURL;
  loading.className = 'hidden'
  resultContainer.appendChild(imageElement);
})

resultContainer.addEventListener('click', function() {
  const link = document.createElement('a')
  if(imageURL) {
    link.href = imageURL
    link.download = 'image_bg.png'
    link.click()
    link.remove()
  }
})
