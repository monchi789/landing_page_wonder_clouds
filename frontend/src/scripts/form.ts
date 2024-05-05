export async function handleRequest(request: { method: string; formData: () => any; }) {
  if (request.method === 'POST') {
    // Prevent default form submission if desired (optional)
    // event.preventDefault();

    const formData = await request.formData();
    const nombre = formData.get('nombre');
    const correo = formData.get('correo');
    const mensaje = formData.get('mensaje');

    // Simulate sending data (replace with your actual sending logic)
    console.log(`Nombre: ${nombre}, Correo: ${correo}, Mensaje: ${mensaje}`);

    // Display success message using an alert or a more user-friendly approach
    alert('¡Mensaje enviado! Gracias por ponerte en contacto.');

    // Optional: Redirect to a confirmation page (consider UX)
    // return new Response('Mensaje enviado', { status: 302, redirect: '/' });
  } else {
    // Handle other HTTP methods (GET, etc.) if needed
    return new Response('Método no permitido', { status: 405 });
  }
}
