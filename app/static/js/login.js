(async function(){
    const fetchData = async (url, method, data) => {
        jsonFetch = {
            method: method,
            cache: 'no-cache',
            body: data
        }
    
        // console.log(jsonFetch)
         const response = await fetch(url, jsonFetch)
         if(!response.ok){
             throw new Error("Error " + url)
         }
    
         return await response.json()
    }

    const $form = document.getElementById("frmLogin")
    $form.addEventListener("submit", async (event)=>{
        event.preventDefault()
        const url = "/login"
        const formData = new FormData($form)
        const response = await fetchData(url, "POST", formData)

        console.log(response)
        
        // VALIDAR RESPUESTA ...
        if(response.error){
            alert(response.message)
        }else{
            window.location.href = response.redirect;
        }
        $form.reset()
    })
})();