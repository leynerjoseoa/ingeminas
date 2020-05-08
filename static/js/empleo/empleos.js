msg('js empleos cargado.');

function msg(msg) {
    console.log(msg);
}

var $ = jQuery.noConflict();

function eliminarya(url, id) {

    $('#btn_' + id).load(
        jQuery.confirm({
                title: 'Estas seguro de Eliminar?',
                //content: 'url:' + url,
                content: 'Eliminar',
                type: 'red',
                icon: 'fa fa-trash',
                animationSpeed: 200, // 0.2 seconds
                onContentReady: function () {
                    // when content is fetched & rendered in DOM
                    var self = this;

                },

                buttons: {
                    ok: function guardar() {

                        console.log('entro al btn ok!');
                        formdata = $('#form-eliminar').serialize();
                        $.ajax({
                            url: url,
                            type: "POST",
                            data: formdata,
                            success: function (status, result) {
                                if (status = 'true') {
                                    console.log('completado.')
                                    eliminarFila(id);

                                    jQuery.confirm({
                                        title: 'Informacion',


                                        animationSpeed: 200, // 0.2 seconds

                                        // animationBounce: 1.5,
                                        content: 'se ha eliminado correctamente',
                                        draggable: true,
                                    });


                                } else {
                                    console.log('no completado.')
                                }
                            },
                            fail: function () {
                                alert("error");
                            }
                        });
                    },
                    close: function () {
                        console.log('click! => no done')
                    }

                },
            }
        )
    )


}


function eliminarFila(id) {
    $('#tr_' + id).hide();
}