<template>
  <nav>
    <router-link to="/">Telegazeta</router-link>
  </nav>
  <div class="container">
    <div class="jumbotron">
        <h1 class="telegazeta"> TELEGAZETA</h1>
    </div>
    <nav class="navbar navbar-expand-lg navbar-light bg-light">
        <div class="collapse navbar-collapse" id="navbarNav">
          <ul class="navbar-nav">
            <li class="nav-item">
              <a class="nav-link" href="#">Telegazeta Online</a>
            </li>
            <li class="nav-item">
              <a class="nav-link" href="#">Ogłoszenia</a>
            </li>
            <li class="nav-item">
              <a class="nav-link" href="#">O nas</a>
            </li>
            <li class="nav-item">
              <a class="nav-link" href="#">Rejestracja</a>
            </li>
            <li class="nav-item">
              <a class="nav-link" href="#">Logowanie</a>
            </li>
          </ul>
        </div>
      </nav>
      <hr class="bg-primary">
      <div class="row-fluid bg-primary">
      <center><router-view/> </center>
      </div>
      <footer>
        <div class="text-center p-3" style="background-color: rgba(0, 0, 0, 0.2);">
    Nie wszystkie prawa zastrzeżone
  </div>
      </footer>
 </div>
</template>

<style src="@/assets/css/bootstrap.css" type="text/css">
</style>
