const form = document.getElementById('predicted_form')

form.addEventListener('submit', (e) => {
    e.preventDefault()
    const formdata = new FormData(e.target)
    const data = {}
    formdata.forEach((value, key) => {
        data[key] = value;
    })
    keys = ['Hours Studied', 'Previous Scores', 'Sleep Hours', 'Sample Question Papers Practiced']
    keys.forEach(i => {
        data[i] = Number(data[i])
    })
    console.log(data)

    fetch('/predict', {
        method: 'POST',
        body: JSON.stringify(data),
        headers: {
            'Content-Type': 'application/json'
        }
    })
    .then(response => response.json())
    .then(result => {
        console.log(result)
        const res = document.getElementById('result')
        res.style.display = 'block';
        res.innerHTML = `<b>Prediction: </b> ${result.prediction}`
    })
})