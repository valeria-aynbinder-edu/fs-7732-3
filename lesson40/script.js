console.log('Inside script.js')

function handleMouseEnter() {
    console.log('mouse entered')
}

const handleMouse = () => {
    console.log('mouse entered')
}

function handleClick(params) {
    console.log('button clicked')
    const elem = document.getElementById('banana')
    elem.innerText = "Apple"
    // elem.className = 'fs-1'
    elem.classList.add('fs-1')

    const kiwiElem = document.getElementById('kiwi')
    kiwiElem.remove()

    const newBtn = document.createElement('button')
    newBtn.innerText = "Another apple"
    newBtn.className = "btn btn-primary"
    newBtn.onmouseenter = () => {
        console.log('mouse entered')
    }
    // newBtn.onmouseenter = handleMouse
    const row = document.getElementsByClassName('row')[0]
    row.appendChild(newBtn)

    // console.log('text', elem.innerText)
    // console.log(elem)
}