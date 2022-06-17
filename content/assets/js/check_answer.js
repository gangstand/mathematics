(function () {
    const btn = document.querySelector('#success')
    const inputs = document.querySelectorAll('.form-check-input')

    btn.style.display = 'none'

    inputs.forEach(checkbox => {
        checkbox.addEventListener('change', () => {
            let isChecked = false
            inputs.forEach(checkbox => {
                if (checkbox.checked) isChecked = true
            })

            if (isChecked) btn.style.display = 'inline-block'
            else btn.style.display = 'none'
        })
    })
})()
