$(document).ready( function (){
    $('#create-list').on("click",'#add-to-list', (e) => {
        e.preventDefault();
        let form = $('#create-list').find('#add-list-form');
        let listContainer = $("#todo-list");
        
        $.ajax({
            url: form.attr("data-addlist-url"),
            data: form.serialize(),
            type : "POST",
            dataType: 'json',
            success: function (data) {
                let element = createElement(data);
                listContainer.append(element)
            }
        });
    });

    $("#todo-list").on("click", ".update-list", function(e){
        e.preventDefault();
        let listId = $(this).data('id')
        $.ajax({
            url: $(this).attr("data-updatelist-url"),
            data: {
                "isDone":Boolean(1),
                "listId":listId,
                "csrfmiddlewaretoken":$("[name='csrfmiddlewaretoken']").val()
            },
            type : "POST",
            dataType: 'json',
            success: function (data) {
                let cloned = $('#todo-list').find(`#list-${listId}`).clone();
                $('#todo-list').find(`#list-${listId}`).remove()
                $('#done-list').append(cloned)
            }
        });
    });

    $("#todo-list").on("click", ".delete-list", function(e){
        e.preventDefault();
        let listId = $(this).data('id');
        $.ajax({
            url: $(this).attr("data-deletelist-url"),
            data: {
                "listId":listId,
                "csrfmiddlewaretoken":$("[name='csrfmiddlewaretoken']").val()
            },
            type : "POST",
            dataType: 'json',
            success: function (data) {
                $('#todo-list').find(`#list-${listId}`).remove()
            }
        });
        

    })
});


function createElement(object) {

    return `<div class="col-md-12 mb-4" id="list-${object.listId}">
        <div class="card border-left-primary shadow py-2">
            <div class="card-body">
            <div class="row no-gutters align-items-center">
                <div class="col-auto">
                    <i class="fas fa-clipboard-list fa-2x text-gray-300"></i>
                </div>
                <div class="col mr-2 ml-4">
                    <div class="text-xs font-weight-bold text-primary text-uppercase mb-1">${object.category}</div>
                    <div class="h5 mb-0 font-weight-bold text-gray-800">${object.description}</div>
                </div>
                <div class="col-auto">
                    <form method="POST" class="update-list-form">
                        <button class="border-0 btn-transition btn btn-outline-success update-list" data-id="${object.listId}" data-updatelist-url="update/list" type="submit"> <i class="fa fa-check"></i></button>
                        <button class="border-0 btn-transition btn btn-outline-danger delete-list"  data-id="${object.listId}" data-deletelist-url="delete/list" type="submit"> <i class="fa fa-trash"></i> </button>
                    </form>
                </div>
            </div>
            </div>
        </div>
    </div>`;
}