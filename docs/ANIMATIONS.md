# Ara 3D Gen - Catalogo de Animacoes

Personagem gerado com o preset: The Soldier
Ferramenta: Ara 3D Gen - https://github.com/olatunde85/3d-gen

---

## Visao Geral

O personagem tem 48 animacoes base distribuidas em 10 categorias.
Todas avaliadas pelo mesmo motor (src/core/anim/evaluate.ts).

- GLB: uma animacao glTF por clip (30 fps, canais rotacao + translacao root)
- FBX: um AnimationStack (take) por clip
- Root motion: disponivel para Walk, Run e Strafe

---

## 1. Idle and Stance

| Clip         | Tipo | Descricao                                      |
|--------------|------|------------------------------------------------|
| Idle         | Loop | Idle relaxado, bracos soltos - pose padrao     |
| Crouch idle  | Loop | Idle em posicao de agachamento                 |

---

## 2. Locomotion

Todos os clips sao loops. Exporta in place ou com root motion.

| Clip            | Tipo | Descricao                                      |
|-----------------|------|------------------------------------------------|
| Walk            | Loop | Caminhada upright, motion capture CMU 07_01    |
| Slouch walk     | Loop | Caminhada com tronco inclinado 13 graus        |
| Run             | Loop | Corrida com motion capture                     |
| Walk backwards  | Loop | Recuo a pe                                     |
| Strafe left     | Loop | Deslocamento lateral esquerda                  |
| Strafe right    | Loop | Deslocamento lateral direita                   |

---

## 3. Actions

| Clip                  | Tipo     | Duracao | Descricao                                      |
|-----------------------|----------|---------|------------------------------------------------|
| Jump                  | One-shot | -       | Salto simples                                  |
| Jump start            | One-shot | 0.45s   | Impulso: agacha, balanco de bracos, decolagem  |
| Jump in air           | Loop     | 0.80s   | Pose aerea com drift. Loop enquanto no ar      |
| Jump land             | One-shot | -       | Aterragem, continua da pose aerea              |
| Running jump          | One-shot | -       | Salto a partir de corrida                      |
| Fall                  | One-shot | -       | Queda livre                                    |
| Punch                 | One-shot | -       | Soco                                           |
| Hit reaction front    | One-shot | -       | Reacao a golpe frente                          |
| Hit reaction back     | One-shot | -       | Reacao a golpe costas                          |
| Hit reaction left     | One-shot | -       | Reacao a golpe esquerda                        |
| Hit reaction right    | One-shot | -       | Reacao a golpe direita                         |
| Knockdown             | One-shot | -       | Tombamento                                     |
| Death fall backward   | One-shot | -       | Morte, cai para tras                           |
| Get up face down      | One-shot | -       | Levanta-se de brucos                           |
| Get up face up        | One-shot | -       | Levanta-se de costas                           |

---

## 4. Emotes

| Clip   | Tipo | Descricao           |
|--------|------|---------------------|
| Wave   | Loop | Acenar com a mao    |
| Cheer  | Loop | Celebracao vitoria  |

---

## 5. Turns

Yaw da anca com passos nos pes. Para rotacoes controladas pelo motor do jogo.

| Clip          | Angulo     |
|---------------|------------|
| Turn left 45  | -45 graus  |
| Turn right 45 | +45 graus  |
| Turn left 90  | -90 graus  |
| Turn right 90 | +90 graus  |
| Turn 360      | 360 graus  |

---

## 6. Shooter

| Clip                  | Tipo     | Descricao                          |
|-----------------------|----------|------------------------------------|
| Pistol idle           | Loop     | Pistola em baixa prontidao         |
| Pistol aim            | One-shot | Levantar pistola para mirar        |
| Pistol fire           | One-shot | Disparar pistola                   |
| Rifle idle            | Loop     | Rifle em baixa prontidao           |
| Rifle aim idle        | Loop     | Rifle em posicao de mira           |
| Rifle fire single     | One-shot | Disparar rifle tiro unico          |
| Rifle fire full-auto  | Loop     | Disparar rifle automatico          |
| Rifle reload          | One-shot | Recarregar rifle                   |
| Aiming walk           | Loop     | Andar em mira                      |
| Aiming walk back      | Loop     | Recuar em mira                     |
| Aiming strafe left    | Loop     | Lateral esquerda em mira           |
| Aiming strafe right   | Loop     | Lateral direita em mira            |
| Rifle run             | Loop     | Correr com rifle                   |
| Sprint                | Loop     | Sprint com rifle                   |
| Crouch aim            | Loop     | Agachar em mira                    |
| Crouch walk           | Loop     | Andar agachado                     |
| Throw grenade         | One-shot | Lancar granada                     |
| Death shooter         | One-shot | Morte, cair em frente              |

---

## 7. Melee

| Clip              | Tipo     | Descricao             |
|-------------------|----------|-----------------------|
| Sword idle guard  | Loop     | Guarda com espada     |
| Sword slash       | One-shot | Corte com espada      |
| Sword block       | One-shot | Bloqueio com espada   |

---

## 8. Sitting and Lying

| Clip                | Tipo     | Descricao               |
|---------------------|----------|-------------------------|
| Sit                 | Loop     | Sentar numa cadeira     |
| Lie down            | One-shot | Deitar-se               |
| Sleep               | Loop     | Deitado a dormir        |
| Get up from sleep   | One-shot | Levantar-se do chao     |

---

## 9. Interactions

| Clip            | Tipo     | Descricao                                      |
|-----------------|----------|------------------------------------------------|
| Ground pickup   | One-shot | Recolher objeto do chao, termina em Carry idle |
| Use press       | One-shot | Usar ou pressionar botao, painel               |
| Open door       | One-shot | Abrir porta                                    |
| Push            | One-shot | Empurrar                                       |
| Carry idle      | Loop     | Idle com objeto agarrado com as duas maos      |
| Carry walk      | Loop     | Andar com objeto, IK de duas maos              |
| Put down drop   | One-shot | Pousar ou largar objeto no chao                |

---

## 10. Vehicles

Animam apenas o rider. O veiculo e fornecido pelo jogo.
Maos posicionadas por IK nos controlos.

| Clip              | Tipo | Altura ancas | Descricao             |
|-------------------|------|--------------|-----------------------|
| Drive car         | Loop | assento      | Conduzir carro        |
| Sit passenger     | Loop | assento      | Passageiro            |
| Ride bicycle      | Loop | 0.93m        | Pedalar bicicleta     |
| Ride motorcycle   | Loop | 0.78m        | Conduzir mota         |
| Ride horse trot   | Loop | 1.40m        | Trote a cavalo        |
| Paddle canoe      | Loop | assento      | Remar canoa           |
| Paddle kayak      | Loop | assento      | Remar kayak           |
| Row boat          | Loop | assento      | Remar barco           |
| Drive boat helm   | Loop | assento      | Conduzir barco        |

---

## Implementar no Godot 4

Passo 1 - No painel de exportacao ativa:
  Mark looping clips in their names
  Os clips ficam nomeados Walk-loop, Idle-loop, etc.

Passo 2 - Importar o GLB:
  Arrasta o .glb para res://characters/ no Godot
  O Godot cria automaticamente um AnimationLibrary

Passo 3 - AnimationPlayer basico:

  @onready var anim = $AnimationPlayer

  func _ready():
      anim.play("Idle-loop")

  func andar():
      anim.play("Walk-loop")

  func saltar():
      anim.play("Jump start")
      await anim.animation_finished
      anim.play("Jump in air-loop")

Passo 4 - Root Motion (se exportaste com Root Motion ativo):

  func _physics_process(delta):
      var rm = anim_tree.get_root_motion_position()
      velocity = rm / delta
      move_and_slide()

---

## Notas Tecnicas

- FPS: 30 fps em todos os clips
- Up axis: +Y, personagem orientado para +Z, pes em y=0
- Game Rig: 65 ossos, nomes Mixamo (Unity Humanoid, Unreal, Mixamo)
- Lite Rig: 25 ossos sem dedos
- Full MakeHuman Rig: 163 ossos inclui rosto
- Crossfade no viewer: 0.25s ao trocar clips
- Grounding automatico: agachamentos, aterragens e passos
- IK de braco dois ossos: maos em armas e veiculos
