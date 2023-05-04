console.log('inside js')

const submitHandler = (event) => {

    event.preventDefault()
    console.log("SUBMITTED")

    const form = event.target
    console.log(form)

    const formData = new FormData(event.target)
    console.log(formData)

    // formData.entries()
    console.log(formData.entries())

    // for (const iterator of formData.entries()) {
    //     console.log(iterator)
    // }

    const data = Object.fromEntries(formData.entries())
    console.log(data)

    console.log(data.email)
    console.log(data['email'])

    const pElem = document.createElement('p')
    pElem.innerText = data.email

    const body = document.getElementsByTagName('body')[0]
    body.appendChild(pElem)
}

// const num = 5
// // num = 6

// let num1 = 5
// num1 = 6

// // let num1 = 8

// var num2 = 5
// num2 = 6

// var num2 = 6