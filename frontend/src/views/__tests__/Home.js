import React from "react";
import chai from "chai";
import {render} from "enzyme";

import Home from "../../views/Home"


let expect = chai.expect;

describe("Home view", function(){
    const HomeTest = class extends Home {
        componentWillMount() {
            this.setState({
                recordscalled: [
                    {
                        "id": 1,
                        "text": "xxxx",
                        "created_date": "2017-08-12",
                        "type": {
                            type: 1
                        },
                        "reason": {
                            reason: 1
                        },
                        "country": {
                            country: 1
                        }
                    }
                ]
            })
        }
    }

    it("should exist the title Sac.", function(){
        const home = render(<HomeTest />);

        const p = home.find("p");
        expect(p.length).to.equal(2);

        expect(p.first().text()).to.equal("Sac");
        expect(p.last().text()).to.equal("Atendimentos");
    });
});
