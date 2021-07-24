(function(){
    const $menu = document.getElementById("menu-api-rest") || null
    if($menu){
        $menu.addEventListener("click", ()=>{
            if($menu.classList.contains("is-active")){
                $menu.classList.remove("is-active")
            }else{
                $menu.classList.add("is-active")
            }
        })
    }

})();
function scroll_to_item(id){
    if(id){
        const $section = document.getElementById(id) || null
        if($section){
            $section.scrollIntoView({
                behavior: 'smooth'
            });
        }
    }
}