import os
import sys

preset = os.environ.get("PRESET", "The Soldier")
out_dir = os.environ.get("OUT_DIR", "docs-out")
os.makedirs(out_dir, exist_ok=True)

# ── ANIMATIONS.md ──────────────────────────────────────────────
animations = """\
# Ara 3D Gen - Catalogo de Animacoes

Personagem gerado com o preset: {preset}
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
""".format(preset=preset)

# ── CUSTOMIZATION.md ───────────────────────────────────────────
customization = """\
# Ara 3D Gen - Guia de Personalizacao

Personagem preset: {preset}
Ferramenta: Ara 3D Gen - https://github.com/olatunde85/3d-gen

---

## Como Funciona

O Ara 3D Gen usa 935 morph targets baseados no dataset CC0 do MakeHuman.
Cada personagem e definido por um ficheiro params.json gerado na exportacao.

Para regenerar ou alterar:
  npm run export -- --params personagem.params.json --out out/

---

## 1. Mudar o Genero

No app web: painel lateral, slider Gender
  0.0 = feminino
  1.0 = masculino
  Valores intermedios = androginia

No params.json:
  {{"gender": 0.8}}

Nota: personagens com idade menor de 18 tem restricoes automaticas de roupa.

---

## 2. Mudar o Rosto

Sliders de forma, painel Face:

| Slider      | Efeito                                 |
|-------------|----------------------------------------|
| Head shape  | Forma geral da cabeca                  |
| Nose        | Largura, comprimento, ponte            |
| Mouth       | Largura, labios                        |
| Eyes        | Tamanho, afastamento, inclinacao       |
| Ears        | Tamanho, posicao                       |
| Chin        | Projecao, largura                      |
| Cheeks      | Volume, projecao                       |

Expressoes (requer v0.2.0):
  neutral, happy, laughing, angry, sad, crying, surprised, afraid, determined

No params.json:
  {{"expression": "happy"}}

A expressao fica como rosto base no export.
GLB: blend shapes para animacao dinamica.
FBX: BlendShape deformer, um canal por shape.

---

## 3. Mudar de Roupa

Tops:
  Tank top, Fatigue shirt, Uniform shirt manga curta ou comprida,
  Techwear jacket, Tattered shirt, Sleeveless tunic,
  Woven tunic (buba), Nenhum shirtless adultos 18+

Bottoms:
  Briefs, Cargo shorts, Fatigue Uniform Techwear Tattered pants,
  Loose trousers (sokoto), Wrappers joelho ou tornozelo,
  Zulu hide aprons, Loincloth, Nenhum adultos 18+

Calcado:
  MakeHuman shoes, Sandals, Combat boots, Descalco

Recolorir roupa:
  Colour - cor principal
  Accent - cor de detalhe (dragonas, cracha, fita refletora)
  Pattern - padrao do tecido

Tecidos: kente, aso-oke, ankara, adire, shuka plaid,
  cowhide, leopard, camo, MOLLE, leather, techwear, tattered

---

## 4. Mudar o Cabelo

Estilos:
  MakeHuman hair, Buzz cut, Punk mohawk liberty spikes,
  Cornrows, Box braids

Cor do cabelo: slider Hair colour

Barba: Stubble, Mustache, Goatee, Short beard, Full beard
Cor da barba: slider Beard colour

---

## 5. Mudar o Corpo

| Slider      | Efeito                             |
|-------------|------------------------------------|
| Gender      | 0 feminino - 1 masculino           |
| Age         | Jovem - Idoso                      |
| Muscle      | Definicao muscular                 |
| Weight      | Peso, massa corporal               |
| Height      | Altura                             |
| Proportions | Proporcoes gerais                  |
| Ethnicity   | Mistura de targets etnicos         |
| Breast      | Volume feminino                    |

Mais 219 sliders de detalhe: cabeca, nariz, boca, olhos, orelhas,
queixo, bochechas, tronco, membros.

---

## 6. Mudar a Pele

20 skins fotorrealistas:
  Faixa etaria: jovem, meia-idade, idoso
  Etnicidade: Africano, Asiatico, Caucasiano
  Sexo: masculino, feminino (automatico)

---

## 7. Presets Disponiveis

| Preset           | Descricao                             |
|------------------|---------------------------------------|
| The Soldier      | Soldado com uniforme de combate       |
| African warrior  | Guerreiro africano                    |
| Yoruba warrior   | Guerreiro Ioruba                      |
| Maasai warrior   | Guerreiro Maasai                      |
| Zulu warrior     | Guerreiro Zulu                        |
| Dahomey warrior  | Guerreiro Daome                       |
| Cyberpunk hacker | Hacker cyberpunk                      |
| Nigerian Police  | Policia nigeriana                     |
| FRSC officer     | Oficial FRSC                          |
| Wasteland surv.  | Sobrevivente pos-apocaliptico         |
| Adventurer       | Aventureiro                           |

Via linha de comandos:
  npm run export -- --preset "The Soldier" --detail high --formats glb,fbx --out out/

Via params.json:
  {{"preset": "The Soldier", "detail": "high"}}

---

## 8. Seeds Aleatorias

  npm run export -- --random 42 --formats glb --out out/

params.json:
  {{"seed": 42}}

---

## 9. Armas e Props

Armas: Assault rifle, Pistol, Sword, Combat knife

Opcoes de exportacao:
  In the hand - arma skinned ao socket WeaponR
  Separate prop - personagem sem arma mais ficheiro separado

Props: Bicycle, Cardboard parcel

---

## 10. Niveis de Detalhe

| Nivel  | Geometria              | Triangulos  |
|--------|------------------------|-------------|
| Low    | Game proxy 1.6k quads  | 5-10k       |
| Medium | Base mesh completa     | 30-40k      |
| High   | Catmull-Clark + roupa  | 100-120k    |

  npm run export -- --preset "The Soldier" --detail low --out out/

---

## 11. Workflow Rapido

1. Exporta o personagem base (ZIP inclui params.json)
2. Edita o params.json com as alteracoes desejadas
3. Reexporta:
     npm run export -- --params personagem.params.json --out out/
4. Resultado tem as mesmas animacoes e rig

---

## 12. Notas para Godot

- Usa GLB para Godot 4 sem plugins
- Ativa Mark looping clips in their names na exportacao
- Esqueleto Game Rig 65 ossos nomes Mixamo e o mais compativel
- Socket WeaponR permite trocar armas no engine sem re-exportar
- Blend shapes das expressoes sao exportados no GLB
""".format(preset=preset)

with open(os.path.join(out_dir, "ANIMATIONS.md"), "w", encoding="utf-8") as f:
    f.write(animations)
print("ANIMATIONS.md gerado.")

with open(os.path.join(out_dir, "CUSTOMIZATION.md"), "w", encoding="utf-8") as f:
    f.write(customization)
print("CUSTOMIZATION.md gerado.")
