import { getGameSession, joinGame } from './GameLogic.js';

export default class GameBoard {
	constructor(appId) {
		this.app = document.querySelector(`#${appId}`);
		this.gameboard = document.createElement('div');
	}

	full_render() {
		this.gameboard.id = "gameModal";
		this.gameboard.classList.add('modal-game');
		this.gameboard.appendChild(this.getDomElements());

		this.app.appendChild(this.gameboard);
		this.afterRender();
	}

	fast_render() {
		this.app.appendChild(this.gameboard);
	}

	getDomElements() {
		// Create the main container div
		const container = document.createElement('div');
		// container.classList.add('board');

		this.paragraph = document.createElement('p');
		this.paragraph.textContent = '';

		const canvas = document.createElement('canvas');
		canvas.id = 'pongCanvas';
		canvas.width = 800;
		canvas.height = 600;
		canvas.classList.add('board');

		container.appendChild(this.paragraph);
		container.appendChild(canvas);

		return container;
	}

	//   startAIgame() {
	//     console.log('AI game started');
	//   }

	async startRemotegame() {
		console.log('Remote game started');

		try {
			const game_id = await getGameSession();
			await joinGame(game_id);
			this.paragraph.textContent = `Game ID: ${game_id}`;
		} catch (error) {
			console.error('Error starting the game: ', error);
		}

		
	}
	
	async afterRender() {

	}
};
