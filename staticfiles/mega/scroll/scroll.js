
const revealElements = document.querySelectorAll("[data-reveal]");

const scrollReveal = function(){
 
	for(let i = 0; i < revealElements.length; i++){
		const isElementsOnScreen =revealElements[i].getBoundingClientRect().top < window.innerHeight;

		if(isElementsOnScreen){
			revealElements[i].classList.add("revealed");
		}else{
			revealElements[i].classList.remove("revealed");
		}
	}
 
}

window.addEventListener("scroll", scrollReveal);
window.addEventListener("load", scrollReveal);


 

const classElements = document.querySelectorAll("[data-class]");

const scrollclass = function(){
 
    for(let i = 0; i < classElements.length; i++){
        const isElementsOnScreen = (classElements[i].getBoundingClientRect().top>0&&classElements[i].getBoundingClientRect().top < window.innerHeight);
        
	
		if(isElementsOnScreen){
            Hakkımızda
            const clasdss =classElements[i].dataset.class;
			classElements[i].classList.add(classElements[i].dataset.class);
		}else{
            Hakkımızda

			classElements[i].classList.remove(classElements[i].dataset.class);
		}
	}
}

window.addEventListener("scroll", scrollclass);
window.addEventListener("load", scrollclass);