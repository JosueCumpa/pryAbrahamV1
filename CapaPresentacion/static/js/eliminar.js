async function eliminar(formulario) {
    
    const id = formulario.querySelector('input[name="id"]').value;


    const result = await Swal.fire({
        title: '¿Estás seguro?',
        text: 'Esta acción no se puede deshacer',
        icon: 'warning',
        showCancelButton: true,
        cancelButtonText: 'NO',
        confirmButtonText: 'SI',
        reverseButtons: false
    });

    if (result.isConfirmed) {
        // Envía el formulario
        formulario.submit();
    }
};