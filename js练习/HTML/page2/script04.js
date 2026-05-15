// alert("Welcome to JavaScript!");


// if(confirm("Are you sure you want to delete this item?")) {
//     alert("Item deleted.");
// } else {
//     alert("Item not deleted.");
// }


var ans = prompt("Are you sure you want to delete this item?", "Type 'yes' to confirm");
if(ans){
    alert("You said: " + ans);
}
else{
    alert("You cancelled the prompt.");
}