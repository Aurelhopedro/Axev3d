# Ara 3D Gen - Guia de Personalizacao

Personagem preset: The Soldier
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
  {"gender": 0.8}

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
  {"expression": "happy"}

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
  {"preset": "The Soldier", "detail": "high"}

---

## 8. Seeds Aleatorias

  npm run export -- --random 42 --formats glb --out out/

params.json:
  {"seed": 42}

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
