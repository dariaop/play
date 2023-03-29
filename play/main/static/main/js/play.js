window.onload = function(){
    let myhp = 100
    let hp = 100
    let flag = 1

    let ag = document.getElementById("ag")
    let at = document.getElementById("at")
    let an = document.getElementById("an")
    let zg = document.getElementById("zg")
    let zt = document.getElementById("zt")
    let zn = document.getElementById("zn")


    ag.onclick = function(){
        if(flag == 1){
            hp-=10
            flag = 0
            document.getElementById("ourhp").innerText = hp
        }
        else{
            alert("вы уже атаковали, защищайтесь")
        }
    }
    at.onclick = function(){
        if(flag == 1){
            hp-=10
            flag = 0
            document.getElementById("ourhp").innerHTML = hp
        }
        else{
            alert("вы уже атаковали, защищайтесь")
        }
    }
    an.onclick = function(){
        if(flag == 1){
            hp-=10
            flag = 0
            document.getElementById("ourhp").innerHTML = hp
        }
        else{
            alert("вы уже атаковали, защищайтесь")
        }
    }
    zg.onclick = function(){
        if(flag == 0){
            myhp-=10
            flag = 1
            document.getElementById("myhp").innerHTML = myhp
        }
        else{
            alert("Атакуйте")
        }
    }
    zt.onclick = function(){
        if(flag == 0){
            myhp-=10
            flag = 1
            document.getElementById("myhp").innerHTML = myhp
        }
        else{
            alert("Атакуйте")
        }
    }
    zn.onclick = function(){
        if(flag == 0){
            myhp-=10
            flag = 1
            document.getElementById("myhp").innerHTML = myhp
        }
        else{
            alert("Атакуйте")
        }
    }

}