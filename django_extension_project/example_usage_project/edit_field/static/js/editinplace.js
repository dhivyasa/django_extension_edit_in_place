$(document).ready(function(){
   console.log("Loading editinplace.js") 
   $(".editinplace_text").editInPlace({
         url: "/edit_field/editinplace",
         element_id: "element_id",
         field_type: "text",
         value_required: false,
         show_buttons: true    });

    $(".editinplace_selectbox").editInPlace({
         url: "/edit_field/editinplace",
         element_id: "element_id",
         field_type: "select",
         select_options:"True,False",
         value_required: false,
         show_buttons: true    });
   console.log("Loaded editinplace.js") 
});
