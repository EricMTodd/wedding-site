console.log("script successful")
window.onload = () => {
    let gallery = document.querySelector("#gallery")

    for (let i = 1; i < 207; i++) {
        let img = document.createElement('img')
        // img.src = `{{url_for('static', filename='images/Caitlyn + Eric-${i}.jpg')}}`
        img.src = `Caitlyn + Eric-${i}.jpg`
        gallery.appendChild(img)
    }

}

