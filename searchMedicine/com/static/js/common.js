function logout(){
    $(location).attr('href', '/logout');
}

function close_pop(){
    $(".popup").hide();
}

function ifNull(val, changeVal){
    if(isNull(val)){
        return changeVal;
    }else{
        return val;
    }
}

// null 이면 truen
function isNull(val){
    if(!val || val == '' || val == 'undifined' || val == 'None' || val == null || val == 'NaN'){
        return true;
    }else{
        return false;
    }
}

function loading(str){
    if(!str){
        loading = "잠시만 기다려 주세요.";
    }

    $("#loading_info").html(str);
    $("#loading_gif").show();
}

function getToday(){
    var now = new Date();
    var year = now.getFullYear();
    var month = now.getMonth() + 1;    //1월이 0으로 되기때문에 +1을 함.
    var date = now.getDate();

    if((month + "").length < 2){        //2자리가 아니면 0을 붙여줌.
        month = "0" + month;
    }else{
        month = "" + month;
    }
    if((date + "").length < 2){        //2자리가 아니면 0을 붙여줌.
        date = "0" + date;
    }else{
        date = "" + date;
    }
    return today = year + month + date;
}

//내약 상세보기
function myMediView(idx){
    var url = "./my_view?idx="+idx
    var ret = window.open(url, "_blank", "toolbar=no,scrollbars=no,resizable=no,top=100,left=100,width=400,height=500");
}

//비밀번호 변경
function change_pwd(){
    $("#chg_pwd").val("");
    $("#chg_pwd2").val("");
    $("#change_pwd_popup").show();
}

function close_pwd_pop(){
    $("#chg_pwd").val("");
    $("#chg_pwd2").val("");
    $("#change_pwd_popup").hide();
}

function action_pwd_chg(){

    var pwd = $("#chg_pwd").val();
    var pwd2 = $("#chg_pwd2").val();

    if(pwd.search(/\s/) != -1){
        alert("비밀번호는 공백 없이 입력해주세요.");
        $("#chg_pwd").val("");
        $("#chg_pwd2").val("");
        return;
    }
    if(pwd.length < 4 || pwd.length > 20){
        alert("비밀번호는 4자리 ~ 20자리로 입력하세요.");
        $("#chg_pwd").val("");
        $("#chg_pwd2").val("");
        return;
    }
    if (pwd != pwd2){
        alert("입력한 비밀번호가 다릅니다! 다시입력하세요.");
        $("#chg_pwd").val("");
        $("#chg_pwd2").val("");
        return;
    }

    if(confirm("변경 하시겠습니까?")){
        form_pwd_chg.submit();
    }

}