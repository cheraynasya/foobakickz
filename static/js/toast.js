function showToast(title, message, type = 'normal', duration = 3000) {
    const toastComponent = document.getElementById('toast-component');
    const toastTitle = document.getElementById('toast-title');
    const toastMessage = document.getElementById('toast-message');
    const toastIcon = document.getElementById('toast-icon');
    
    if (!toastComponent) return;

    toastComponent.classList.remove(
        'bg-red-50', 'border-red-500', 'text-red-600', 'border-l-red-500',
        'bg-green-50', 'border-green-500', 'text-green-600', 'border-l-green-500',
        'bg-yellow-50', 'border-yellow-500', 'text-yellow-600', 'border-l-yellow-500',
        'bg-white', 'border-gray-300', 'text-gray-800', 'border-l-gray-500'
    );
    toastIcon.innerHTML = ''; 

    if (type === 'success') {
        toastComponent.classList.add('bg-green-50', 'border-l-green-500', 'text-green-600');
        toastTitle.classList.add('text-green-800');
        toastMessage.classList.add('text-green-700');
        toastIcon.innerHTML = '✅';
    } else if (type === 'error') {
        toastComponent.classList.add('bg-red-50', 'border-l-red-500', 'text-red-600');
        toastTitle.classList.add('text-red-800');
        toastMessage.classList.add('text-red-700');
        toastIcon.innerHTML = '❌';
    } else if (type === 'warning') {
        toastComponent.classList.add('bg-yellow-50', 'border-l-yellow-500', 'text-yellow-600');
        toastTitle.classList.add('text-yellow-800');
        toastMessage.classList.add('text-yellow-700');
        toastIcon.innerHTML = '⚠️';
    } else {
        toastComponent.classList.add('bg-white', 'border-l-gray-500', 'text-gray-800');
        toastTitle.classList.add('text-gray-900');
        toastMessage.classList.add('text-gray-700');
        toastIcon.innerHTML = '🔔';
    }

    toastTitle.textContent = title;
    toastMessage.textContent = message;

    toastComponent.classList.remove('opacity-0', 'translate-y-64');
    toastComponent.classList.add('opacity-100', 'translate-y-0');

    setTimeout(() => {
        toastComponent.classList.remove('opacity-100', 'translate-y-0');
        toastComponent.classList.add('opacity-0', 'translate-y-64');
    }, duration);
}