<template>
    <header class="header">
      <div class="logo">
        <h1>TrackTracer</h1>
      </div>
      <div class="menu">
        <button id="open-menu-button">
          <img src="@/assets/images/menu-icon.png" alt="Menu" />
        </button>
      </div>
    </header>
  </template>
  
  <script>
  export default {
    name: "Header",
  };
  </script>
  
  <style scoped>
  .header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 10px 20px;
    background-color: #333;
    color: #fff;
  }
  </style>
  