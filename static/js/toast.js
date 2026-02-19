function showToast(title, message, type = 'normal', duration = 3000) {
  const toastComponent = document.getElementById('toast-component');
  const toastTitle = document.getElementById('toast-title');
  const toastMessage = document.getElementById('toast-message');
  if (!toastComponent) return;

  const bg = (type === 'error') ? '#EF4444' : '#8BC34A';
  toastComponent.style.background = bg;
  toastComponent.style.color = '#fff';
  toastComponent.style.border = 'none';

  if (toastTitle) toastTitle.style.color = '#fff';
  if (toastMessage) toastMessage.style.color = '#fff';

  toastTitle.textContent = title || '';
  toastMessage.textContent = message || '';

  toastComponent.classList.remove('opacity-0', 'translate-y-64');
  toastComponent.classList.add('opacity-100', 'translate-y-0');

  clearTimeout(toastComponent._timer);
  toastComponent._timer = setTimeout(() => {
    toastComponent.classList.remove('opacity-100', 'translate-y-0');
    toastComponent.classList.add('opacity-0', 'translate-y-64');
  }, duration);
}
